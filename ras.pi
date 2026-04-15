import cv2
from ultralytics import YOLO
from deepface import DeepFace
import os

# --- 1. CONFIGURATION ---
# Use the smallest model possible (YOLOv8n or v11n)
model = YOLO("yolov8n.pt") 

# Target image path (Hardcode it for the Pi to avoid Tkinter issues in flight)
target_path = "target.jpg" 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("--- DRONE TACTICAL SYSTEM STARTING ---")

frame_count = 0
skip_frames = 5  # Only run Face ID every 5 frames to save CPU

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    frame_count += 1
    
    # 1. Fast YOLO Detection
    results = model.track(frame, persist=True, verbose=False, imgsz=320) # Small imgsz = Faster
    
    annotated_frame = frame.copy()

    if results and results[0].boxes:
        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            
            if model.names[cls_id] == "person":
                color = (0, 255, 0)
                label = "Person"

                # 2. Heavy Face Recognition (Only every X frames)
                if frame_count % skip_frames == 0:
                    try:
                        face_crop = frame[y1:y2, x1:x2]
                        if face_crop.size > 0:
                            verify = DeepFace.verify(
                                img1_path=target_path, 
                                img2_path=face_crop,
                                model_name="VGG-Face",
                                enforce_detection=False,
                                detector_backend="opencv"
                            )
                            if verify["verified"]:
                                color = (0, 0, 255)
                                label = "TARGET MATCH!"
                    except:
                        pass

                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(annotated_frame, label, (x1, y1 - 10), 1, 1, color, 2)

    cv2.imshow("Pi Drone Vision", annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
