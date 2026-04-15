#!/usr/bin/env python3
"""
MECA DRONE - AI Integration Module
Connects person detection with desktop application and backend services
"""

import cv2
import numpy as np
import threading
import time
import json
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import sys
import os

# Add AI modules to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

@dataclass
class DetectionResult:
    """Detection result data structure"""
    detected: bool
    target_identified: bool
    confidence: float
    bbox: List[int]
    center: Tuple[int, int]
    timestamp: float
    target_locked: bool = False
    match_score: float = 0.0

class PersonDetectionIntegration:
    """Integration layer for person detection system"""
    
    def __init__(self):
        self.detection_active = False
        self.current_target = None
        self.detection_thread = None
        self.camera = None
        self.model = None
        self.callbacks = {
            'on_detection': None,
            'on_target_lock': None,
            'on_error': None
        }
        
    def initialize_detection(self, target_image_path: Optional[str] = None) -> bool:
        """Initialize the detection system"""
        try:
            # Import detection modules
            from ultralytics import YOLO
            from deepface import DeepFace
            
            # Load YOLO model
            self.model = YOLO("yolov8n.pt")  # Use lightweight model
            
            # Set target if provided
            if target_image_path and os.path.exists(target_image_path):
                self.current_target = target_image_path
                print(f"Target loaded: {os.path.basename(target_image_path)}")
            
            # Initialize camera
            self.camera = cv2.VideoCapture(0)
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            
            return True
            
        except Exception as e:
            self._handle_error(f"Detection initialization failed: {str(e)}")
            return False
    
    def start_detection(self) -> bool:
        """Start the detection process"""
        if self.detection_active:
            return True
            
        if not self.model or not self.camera:
            if not self.initialize_detection():
                return False
        
        self.detection_active = True
        self.detection_thread = threading.Thread(target=self._detection_loop, daemon=True)
        self.detection_thread.start()
        
        print("Person detection started")
        return True
    
    def stop_detection(self):
        """Stop the detection process"""
        self.detection_active = False
        if self.camera:
            self.camera.release()
        print("Person detection stopped")
    
    def _detection_loop(self):
        """Main detection loop running in separate thread"""
        frame_count = 0
        skip_frames = 5  # Process face recognition every 5 frames
        
        while self.detection_active and self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            if not ret:
                break
            
            frame_count += 1
            
            try:
                # YOLO detection
                results = self.model.track(frame, persist=True, verbose=False)
                
                if results and results[0].boxes:
                    for box in results[0].boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])
                        cls_id = int(box.cls[0])
                        
                        if self.model.names[cls_id] == "person":
                            # Create detection result
                            result = DetectionResult(
                                detected=True,
                                target_identified=False,
                                confidence=float(box.conf[0]),
                                bbox=[x1, y1, x2, y2],
                                center=((x1 + x2) // 2, (y1 + y2) // 2),
                                timestamp=time.time()
                            )
                            
                            # Face recognition (every few frames for performance)
                            if self.current_target and frame_count % skip_frames == 0:
                                try:
                                    person_crop = frame[y1:y2, x1:x2]
                                    if person_crop.size > 0:
                                        verify = DeepFace.verify(
                                            img1_path=self.current_target,
                                            img2_path=person_crop,
                                            model_name="VGG-Face",
                                            enforce_detection=False,
                                            detector_backend="opencv"
                                        )
                                        
                                        if verify["verified"]:
                                            result.target_identified = True
                                            result.target_locked = True
                                            result.match_score = (1 - verify["distance"]) * 100
                                            
                                            # Notify target lock
                                            if self.callbacks['on_target_lock']:
                                                self.callbacks['on_target_lock'](result)
                                
                                except Exception as e:
                                    # Face recognition failed, continue with person detection
                                    pass
                            
                            # Notify detection
                            if self.callbacks['on_detection']:
                                self.callbacks['on_detection'](result)
            
            except Exception as e:
                self._handle_error(f"Detection error: {str(e)}")
                break
            
            # Small delay to prevent CPU overload
            time.sleep(0.03)  # ~30 FPS
    
    def set_target(self, target_image_path: str) -> bool:
        """Set or update the target image"""
        if os.path.exists(target_image_path):
            self.current_target = target_image_path
            print(f"Target updated: {os.path.basename(target_image_path)}")
            return True
        return False
    
    def get_current_frame(self) -> Optional[np.ndarray]:
        """Get current camera frame"""
        if self.camera and self.camera.isOpened():
            ret, frame = self.camera.read()
            return frame if ret else None
        return None
    
    def register_callback(self, event: str, callback):
        """Register callback for detection events"""
        if event in self.callbacks:
            self.callbacks[event] = callback
    
    def _handle_error(self, error_message: str):
        """Handle errors and notify callbacks"""
        print(f"AI Error: {error_message}")
        if self.callbacks['on_error']:
            self.callbacks['on_error'](error_message)
    
    def get_status(self) -> Dict:
        """Get current detection status"""
        return {
            'active': self.detection_active,
            'target_loaded': self.current_target is not None,
            'target_name': os.path.basename(self.current_target) if self.current_target else None,
            'camera_active': self.camera is not None and self.camera.isOpened()
        }

class DesktopAppIntegration:
    """Integration with MECA DRONE desktop application"""
    
    def __init__(self, desktop_app):
        self.desktop_app = desktop_app
        self.ai_detector = PersonDetectionIntegration()
        self.setup_callbacks()
    
    def setup_callbacks(self):
        """Setup AI detection callbacks"""
        self.ai_detector.register_callback('on_detection', self._on_detection)
        self.ai_detector.register_callback('on_target_lock', self._on_target_lock)
        self.ai_detector.register_callback('on_error', self._on_error)
    
    def _on_detection(self, result: DetectionResult):
        """Handle person detection"""
        # Update desktop app with detection info
        if hasattr(self.desktop_app, 'update_detection_status'):
            self.desktop_app.update_detection_status({
                'persons_detected': 1,
                'confidence': result.confidence,
                'position': result.center,
                'timestamp': result.timestamp
            })
    
    def _on_target_lock(self, result: DetectionResult):
        """Handle target identification"""
        # Update desktop app with target lock
        if hasattr(self.desktop_app, 'update_target_status'):
            self.desktop_app.update_target_status({
                'target_locked': True,
                'match_score': result.match_score,
                'position': result.center,
                'bbox': result.bbox,
                'timestamp': result.timestamp
            })
        
        print(f"🎯 TARGET LOCKED! Match: {result.match_score:.1f}%")
    
    def _on_error(self, error_message: str):
        """Handle AI errors"""
        if hasattr(self.desktop_app, 'show_error'):
            self.desktop_app.show_error(f"AI Detection Error: {error_message}")
    
    def start_ai_detection(self, target_path: Optional[str] = None) -> bool:
        """Start AI detection from desktop app"""
        return self.ai_detector.start_detection() and self.ai_detector.set_target(target_path or "")
    
    def stop_ai_detection(self):
        """Stop AI detection"""
        self.ai_detector.stop_detection()
    
    def get_ai_status(self) -> Dict:
        """Get AI system status"""
        return self.ai_detector.get_status()

# Example usage with desktop app
def integrate_with_desktop_app(desktop_app_instance):
    """Integrate AI detection with desktop application"""
    integration = DesktopAppIntegration(desktop_app_instance)
    
    # Add AI controls to desktop app
    if hasattr(desktop_app_instance, 'add_ai_controls'):
        desktop_app_instance.add_ai_controls(integration)
    
    return integration

if __name__ == "__main__":
    # Test the integration
    print("🤖 MECA DRONE AI Integration Test")
    print("=" * 50)
    
    detector = PersonDetectionIntegration()
    
    # Test initialization
    if detector.initialize_detection():
        print("✅ Detection system initialized")
        
        # Test detection
        if detector.start_detection():
            print("✅ Detection started")
            
            # Run for 10 seconds
            time.sleep(10)
            
            detector.stop_detection()
            print("✅ Detection stopped")
        else:
            print("❌ Failed to start detection")
    else:
        print("❌ Failed to initialize detection")
