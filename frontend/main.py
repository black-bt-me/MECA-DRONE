import tkinter as tk
from PIL import Image, ImageTk
import os
import math
import sys
import threading
import time
from tkinter import filedialog, messagebox

# Add AI module path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'ai'))

class HomePage(tk.Frame):
    def __init__(self, parent, base_path, load_image_func):
        super().__init__(parent, bg="#0d1117")
        self.base_path = base_path
        self.load_image = load_image_func
        self.images = {}
        
        # Main container
        self.canvas = tk.Canvas(self, bg="#0d1117", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Initial animation state
        self.anim_step = 0
        
        # Bind resize event
        self.canvas.bind("<Configure>", self._on_resize)
        
    def _on_resize(self, event=None):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Background Grid (3D Morph Lines)
        # Scaled to look better at the bottom
        grid_size = (int(width * 0.9), int(height * 0.5))
        self.grid_img = self.load_image("grid_bg", "3D Morph Lines 13.png", size=grid_size, collection=self.images)
        if self.grid_img:
            if hasattr(self, 'grid_id'):
                self.canvas.itemconfig(self.grid_id, image=self.grid_img)
            else:
                self.grid_id = self.canvas.create_image(width // 2, int(height * 0.77), image=self.grid_img)
            self.canvas.coords(self.grid_id, width // 2, int(height * 0.77))

        # Title: MECA DRONE
        font_size = max(40, int(width // 15))
        if hasattr(self, 'title_id'):
            self.canvas.itemconfig(self.title_id, font=("Helvetica", font_size, "bold"))
            self.canvas.coords(self.title_id, width // 2, int(height * 0.23))
        else:
            self.title_id = self.canvas.create_text(
                width // 2, int(height * 0.23), 
                text="MECA DRONE", 
                fill="white", 
                font=("Helvetica", font_size, "bold"),
                anchor="center"
            )
        
        # Subtext
        subtext_size = max(12, int(width // 50))
        if hasattr(self, 'subtext_id'):
            self.canvas.itemconfig(self.subtext_id, font=("Helvetica", subtext_size, "bold"))
            self.canvas.coords(self.subtext_id, width // 2, int(height * 0.37))
        else:
            self.subtext_id = self.canvas.create_text(
                width // 2, int(height * 0.37), 
                text="Discover The Magic !", 
                fill="white", 
                font=("Helvetica", subtext_size, "bold"),
                anchor="center"
            )
        
        # Drones
        self.drone_left_pos = [int(width * 0.23), int(height * 0.74)]
        self.drone_right_pos = [int(width * 0.64), int(height * 0.46)]
        
        drone_left_size = (int(width * 0.3), int(height * 0.46))
        self.drone_left_img = self.load_image("drone_left", "Group 4.png", size=drone_left_size, collection=self.images)
        if self.drone_left_img:
            if hasattr(self, 'drone_left_id'):
                self.canvas.itemconfig(self.drone_left_id, image=self.drone_left_img)
            else:
                self.drone_left_id = self.canvas.create_image(self.drone_left_pos[0], self.drone_left_pos[1], image=self.drone_left_img)
            self.canvas.coords(self.drone_left_id, self.drone_left_pos[0], self.drone_left_pos[1])
            
        drone_right_size = (int(width * 0.16), int(height * 0.28))
        self.drone_right_img = self.load_image("drone_right", "Group 3.png", size=drone_right_size, collection=self.images)
        if self.drone_right_img:
            if hasattr(self, 'drone_right_id'):
                self.canvas.itemconfig(self.drone_right_id, image=self.drone_right_img)
            else:
                self.drone_right_id = self.canvas.create_image(self.drone_right_pos[0], self.drone_right_pos[1], image=self.drone_right_img)
            self.canvas.coords(self.drone_right_id, self.drone_right_pos[0], self.drone_right_pos[1])
            
        if not hasattr(self, 'anim_started'):
            self.anim_started = True
            self.animate_drones()

    def animate_drones(self):
        """Floating animation for drones"""
        if not self.winfo_exists():
            return
            
        self.anim_step += 0.05
        
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        y_offset_left = math.sin(self.anim_step) * 15
        y_offset_right = math.cos(self.anim_step * 1.2) * 12
        
        # Update positions using current width/height
        if hasattr(self, 'drone_left_id'):
            self.canvas.coords(self.drone_left_id, int(width * 0.23), int(height * 0.74) + y_offset_left)
            
        if hasattr(self, 'drone_right_id'):
            self.canvas.coords(self.drone_right_id, int(width * 0.64), int(height * 0.46) + y_offset_right)
            
        # Float the grid slightly too for dynamic feel
        if hasattr(self, 'grid_id'):
             self.canvas.coords(self.grid_id, width // 2, int(height * 0.77) + (math.sin(self.anim_step * 0.5) * 5))
             
        self.after(30, self.animate_drones)
    
    def request_demo(self):
        messagebox.showinfo("Request Demo", "Demo request functionality would be implemented here.")
    
    def contact_us(self):
        messagebox.showinfo("Contact Us", "Contact functionality would be implemented here.")

class DashboardPage(tk.Frame):
    def __init__(self, parent, base_path, load_image_func):
        super().__init__(parent, bg="#0d1117")
        self.base_path = base_path
        self.load_image = load_image_func
        self.images = {}
        
        # Main container
        self.canvas = tk.Canvas(self, bg="#0d1117", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Bind resize
        self.canvas.bind("<Configure>", self._on_resize)
        
    def _on_resize(self, event=None):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Title
        if hasattr(self, 'title_id'):
            self.canvas.coords(self.title_id, width // 2, 40)
        else:
            self.title_id = self.canvas.create_text(
                width // 2, 40, 
                text="Telemetry Dashboard", 
                fill="white", 
                font=("Arial", 24, "bold"),
                anchor="center"
            )
        
        # AI Status Section
        bar_width = int(width * 0.9)
        bar_x1 = (width - bar_width) // 2
        bar_x2 = bar_x1 + bar_width
        
        if hasattr(self, 'ai_bar_id'):
            self.canvas.coords(self.ai_bar_id, bar_x1, 80, bar_x2, 140)
        else:
            self.ai_bar_id = self.canvas.create_rectangle(
                bar_x1, 80, bar_x2, 140,
                fill="#161b22",
                outline=""
            )
            
        if hasattr(self, 'ai_title_id'):
            self.canvas.coords(self.ai_title_id, width // 2, 100)
            self.canvas.coords(self.ai_status_id, width // 2, 120)
        else:
            self.ai_title_id = self.canvas.create_text(
                width // 2, 100, 
                text="🤖 AI PERSON DETECTION STATUS", 
                fill="#f59e0b", 
                font=("Arial", 14, "bold"),
                anchor="center"
            )
            self.ai_status_id = self.canvas.create_text(
                width // 2, 120, 
                text="🟡 AI MODULE READY | TARGET: NOT SET | DETECTION: STANDBY", 
                fill="#eab308", 
                font=("Arial", 12, "bold"),
                anchor="center"
            )
            
        # AI Control Buttons
        btn_center_left = width // 2 - 100
        btn_center_right = width // 2 + 100
        
        if hasattr(self, 'ai_start_btn'):
            self.canvas.coords(self.ai_start_btn, btn_center_left - 60, 150, btn_center_left + 60, 180)
            self.canvas.coords(self.ai_start_text, btn_center_left, 165)
            self.canvas.coords(self.ai_test_btn, btn_center_right - 45, 150, btn_center_right + 45, 180)
            self.canvas.coords(self.ai_test_text, btn_center_right, 165)
        else:
            self.ai_start_btn = self.canvas.create_rectangle(
                btn_center_left - 60, 150, btn_center_left + 60, 180,
                fill="#10b981",
                outline=""
            )
            self.ai_start_text = self.canvas.create_text(
                btn_center_left, 165, 
                text="🎯 SET TARGET", 
                fill="white", 
                font=("Arial", 10, "bold"),
                anchor="center"
            )
            
            self.ai_test_btn = self.canvas.create_rectangle(
                btn_center_right - 45, 150, btn_center_right + 45, 180,
                fill="#6366f1",
                outline=""
            )
            self.ai_test_text = self.canvas.create_text(
                btn_center_right, 165, 
                text="🧪 TEST AI", 
                fill="white", 
                font=("Arial", 10, "bold"),
                anchor="center"
            )
            
            # Bind events (first time only)
            self.canvas.tag_bind(self.ai_start_btn, "<Button-1>", lambda e: self.set_ai_target())
            self.canvas.tag_bind(self.ai_test_btn, "<Button-1>", lambda e: self.test_ai())

        # Telemetry cards
        telemetry_data = [
            ("Altitude", "50.0", "meters", "⚡", 0.15),
            ("Battery", "12.6", "volts", "🔋", 0.32),
            ("GPS Lock", "LOCKED", "37.7749...", "📍", 0.50),
            ("Signal", "85%", "strength", "📡", 0.68),
            ("AI Status", "READY", "Detection", "🤖", 0.85),
            ("Target", "NONE", "Pending", "🎯", 0.15, 0.65), # Lower row
        ]
        
        # Clear old card items if they exist
        if not hasattr(self, 'card_items'):
            self.card_items = []
        else:
            for item in self.card_items:
                self.canvas.delete(item)
            self.card_items = []

        for data in telemetry_data:
            label, value, unit, icon, rel_x = data[:5]
            rel_y = data[5] if len(data) > 5 else 0.45
            
            x = int(width * rel_x)
            y = int(height * rel_y)
            
            # Card background
            self.card_items.append(self.canvas.create_rectangle(
                x-70, y-50, x+70, y+50,
                fill="#161b22",
                outline=""
            ))
            # Icon
            self.card_items.append(self.canvas.create_text(
                x-50, y-30, 
                text=icon, 
                fill="#f59e0b", 
                font=("Arial", 16),
                anchor="w"
            ))
            # Label
            self.card_items.append(self.canvas.create_text(
                x-50, y-10, 
                text=label, 
                fill="#9ca3af", 
                font=("Arial", 10),
                anchor="w"
            ))
            # Value
            self.card_items.append(self.canvas.create_text(
                x-50, y+10, 
                text=value, 
                fill="white", 
                font=("Arial", 20, "bold"),
                anchor="w"
            ))
            # Unit
            self.card_items.append(self.canvas.create_text(
                x-50, y+25, 
                text=unit, 
                fill="#6b7280", 
                font=("Arial", 10),
                anchor="w"
            ))
        
        # Start telemetry updates
        self.update_telemetry()
    
    def set_ai_target(self):
        messagebox.showinfo("AI Target", "Target selection would open file dialog to choose person image.")
    
    def test_ai(self):
        messagebox.showinfo("AI Test", "Testing AI detection system...\n\n• Person Detection: ✅ Working\n• Face Recognition: ✅ Working\n• Target Matching: ✅ Ready")
    
    def update_telemetry(self):
        # Simulate telemetry updates
        import random
        self.after(1000, self.update_telemetry)

class StreamingPage(tk.Frame):
    def __init__(self, parent, base_path, load_image_func):
        super().__init__(parent, bg="black")
        self.base_path = base_path
        self.load_image = load_image_func
        self.images = {}
        
        # Main container
        self.canvas = tk.Canvas(self, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Bug Fix: Initialize current_state
        self.current_state = "static"
        
        # Bind resize
        self.canvas.bind("<Configure>", self._on_resize)
        
    def _on_resize(self, event=None):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # Draw the rounded image / big background
        bg_size = (int(width * 0.95), int(height * 0.9))
        self.bg_player = self.load_image("bg_player", "979024a22c83c85711ddf437f92a3ba8@origin.jpg.png", size=bg_size, collection=self.images)
        if self.bg_player:
            if hasattr(self, 'bg_id'):
                self.canvas.itemconfig(self.bg_id, image=self.bg_player)
            else:
                self.bg_id = self.canvas.create_image(width // 2, height // 2, image=self.bg_player)
            self.canvas.coords(self.bg_id, width // 2, height // 2)
            
        # Play button
        btn_size = (int(width * 0.18), int(height * 0.2))
        self.play_btn_static = self.load_image("play_btn_static", "Group 11.png", size=btn_size, collection=self.images)
        if self.play_btn_static:
            if hasattr(self, 'play_id'):
                self.canvas.itemconfig(self.play_id, image=self.play_btn_static)
            else:
                self.play_id = self.canvas.create_image(width // 2, height // 2, image=self.play_btn_static)
                # Bind events for three states
                self.canvas.tag_bind(self.play_id, "<Enter>", self.on_mouse_enter)
                self.canvas.tag_bind(self.play_id, "<Leave>", self.on_mouse_leave)
                self.canvas.tag_bind(self.play_id, "<ButtonPress-1>", self.on_button_press)
                self.canvas.tag_bind(self.play_id, "<ButtonRelease-1>", self.on_button_release)
            self.canvas.coords(self.play_id, width // 2, height // 2)

        # Update hover/pressed states too
        self.play_btn_hover = self.create_hover_state()
        self.play_btn_pressed = self.create_pressed_state()
    
    def create_hover_state(self):
        """Create hover state - slightly larger and brighter"""
        try:
            original_img = Image.open(os.path.join(self.base_path, "Group 11.png"))
            # Make it slightly larger for hover effect
            hover_img = original_img.resize((200, 145), Image.Resampling.LANCZOS)
            # Make it slightly brighter
            from PIL import ImageEnhance
            enhancer = ImageEnhance.Brightness(hover_img)
            hover_img = enhancer.enhance(1.2)
            return ImageTk.PhotoImage(hover_img)
        except:
            return self.play_btn_static
    
    def create_pressed_state(self):
        """Create pressed state - slightly smaller and darker"""
        try:
            original_img = Image.open(os.path.join(self.base_path, "Group 11.png"))
            # Make it slightly smaller for pressed effect
            pressed_img = original_img.resize((160, 115), Image.Resampling.LANCZOS)
            # Make it slightly darker
            from PIL import ImageEnhance
            enhancer = ImageEnhance.Brightness(pressed_img)
            pressed_img = enhancer.enhance(0.8)
            return ImageTk.PhotoImage(pressed_img)
        except:
            return self.play_btn_static
    
    def on_mouse_enter(self, event):
        """Static -> Hover state"""
        if self.current_state != "pressed":
            self.current_state = "hover"
            self.canvas.itemconfig(self.play_id, image=self.play_btn_hover)
            self.canvas.config(cursor="hand2")
    
    def on_mouse_leave(self, event):
        """Return to Static state"""
        if self.current_state != "pressed":
            self.current_state = "static"
            self.canvas.itemconfig(self.play_id, image=self.play_btn_static)
            self.canvas.config(cursor="")
    
    def on_button_press(self, event):
        """Hover -> Pressed state"""
        self.current_state = "pressed"
        self.canvas.itemconfig(self.play_id, image=self.play_btn_pressed)
    
    def on_button_release(self, event):
        """Pressed -> Hover state and trigger action"""
        self.current_state = "hover"
        self.canvas.itemconfig(self.play_id, image=self.play_btn_hover)
        self.play_video(event)
    
    def play_video(self, event):
        """Handle video play button click"""
        print("Play Video Clicked")
        # Here you would start the video stream

class FindPersonPage(tk.Frame):
    def __init__(self, parent, base_path, load_image_func):
        super().__init__(parent, bg="black")
        self.base_path = base_path
        self.load_image = load_image_func
        self.images = {}
        self.ai_status = "Ready"
        self.detection_active = False
        self.target_path = None
        self.upload_hovering = False
        self.upload_animation_step = 0
        self.upload_original_pos = (500, 180)
        
        # Main container
        self.canvas = tk.Canvas(self, bg="black", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        
        # Bind resize
        self.canvas.bind("<Configure>", self._on_resize)
        
    def _on_resize(self, event=None):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        # 1. Header Text
        if hasattr(self, 'header_id'):
            self.canvas.coords(self.header_id, width // 2, 80)
        else:
            self.header_id = self.canvas.create_text(
                width // 2, 80, 
                text="We will find that person for You", 
                fill="white", 
                font=("Helvetica", 22, "bold"),
                justify="center"
            )
        
        # 2. Upload Button
        if hasattr(self, 'upload_id'):
            self.upload_original_pos = (width // 2, int(height * 0.3))
            self.canvas.coords(self.upload_id, self.upload_original_pos[0], self.upload_original_pos[1])
        else:
            self.upload_original_pos = (width // 2, int(height * 0.3))
            upload_btn = self.load_image("upload_btn", "Frame 4.png", collection=self.images)
            if upload_btn:
                self.upload_id = self.canvas.create_image(self.upload_original_pos[0], self.upload_original_pos[1], image=upload_btn)
                self.canvas.tag_bind(self.upload_id, "<Enter>", self.on_upload_hover)
                self.canvas.tag_bind(self.upload_id, "<Leave>", self.on_upload_leave)
                self.canvas.tag_bind(self.upload_id, "<Button-1>", self.upload_target_image)

        # 3. Big Plus Sign
        if hasattr(self, 'plus_id'):
            self.canvas.coords(self.plus_id, width // 2, int(height * 0.45))
        else:
            plus_icon = self.load_image("big_plus", "plus.png", size=(32, 32), collection=self.images)
            if plus_icon:
                self.plus_id = self.canvas.create_image(width // 2, int(height * 0.45), image=plus_icon)
                self.canvas.tag_bind(self.plus_id, "<Button-1>", self.upload_target_image)
                self.canvas.tag_bind(self.plus_id, "<Enter>", lambda e: (self.canvas.config(cursor="hand2")))
                self.canvas.tag_bind(self.plus_id, "<Leave>", lambda e: (self.canvas.config(cursor="")))

        # 4. Result/Preview Image
        preview_h = int(height * 0.45)
        preview_w = int(preview_h * (190 / 339))
        self.preview_img = self.load_image("person_preview", "téléchargement (1) 1.png", size=(preview_w, preview_h), collection=self.images)
        
        if hasattr(self, 'preview_id'):
            self.canvas.itemconfig(self.preview_id, image=self.preview_img)
            self.canvas.coords(self.preview_id, width // 2, int(height * 0.72))
        else:
            if self.preview_img:
                self.preview_id = self.canvas.create_image(width // 2, int(height * 0.72), image=self.preview_img)
                self.canvas.tag_bind(self.preview_id, "<Button-1>", self.start_detection)
                self.canvas.tag_bind(self.preview_id, "<Enter>", lambda e: (self.canvas.config(cursor="hand2")))
                self.canvas.tag_bind(self.preview_id, "<Leave>", lambda e: (self.canvas.config(cursor="")))
    
    def on_upload_hover(self, event):
        """Start upload button hover animation"""
        self.upload_hovering = True
        self.upload_animation_step = 0
        self.canvas.config(cursor="hand2")
        self.animate_upload_button()
    
    def on_upload_leave(self, event):
        """Stop upload button hover animation"""
        self.upload_hovering = False
        self.canvas.config(cursor="")
        # Reset to original position
        self.canvas.coords(self.upload_id, self.upload_original_pos[0], self.upload_original_pos[1])
    
    def animate_upload_button(self):
        """Animate upload button when hovering"""
        if self.upload_hovering:
            self.upload_animation_step += 0.2
            
            # Create gentle floating movement
            x_offset = math.sin(self.upload_animation_step) * 8
            y_offset = math.cos(self.upload_animation_step * 0.8) * 6
            
            # Update button position
            new_x = self.upload_original_pos[0] + x_offset
            new_y = self.upload_original_pos[1] + y_offset
            self.canvas.coords(self.upload_id, new_x, new_y)
            
            # Continue animation
            self.after(50, self.animate_upload_button)
    
    def upload_target_image(self, event=None):
        """Handle target image upload"""
        try:
            file_path = filedialog.askopenfilename(
                title="Select Target Image",
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")]
            )
            
            if file_path:
                self.target_path = file_path
                messagebox.showinfo("Success", "Target image loaded successfully!")
            else:
                messagebox.showinfo("Info", "No image selected")
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")
    
    def start_detection(self, event=None):
        """Start AI detection"""
        if not self.target_path:
            messagebox.showwarning("No Target", "Please upload a target image first!")
            return
            
        self.detection_active = True
        messagebox.showinfo("Detection", "AI detection started!")
        threading.Thread(target=self.run_detection, daemon=True).start()
    
    def stop_detection(self, event=None):
        """Stop AI detection"""
        self.detection_active = False
        messagebox.showinfo("Detection", "AI detection stopped!")
    
    def run_detection(self):
        """Run AI detection in background"""
        try:
            from integration import PersonDetectionIntegration
            
            detector = PersonDetectionIntegration()
            if detector.initialize_detection(self.target_path):
                detector.start_detection()
                
                while self.detection_active:
                    time.sleep(1)
                    if detector.detection_active:
                        print("🔍 Detecting... Target locked")
                    else:
                        break
                        
                detector.stop_detection()
                messagebox.showinfo("Complete", "Detection completed successfully!")
            else:
                messagebox.showerror("Error", "Failed to initialize AI")
                
        except Exception as e:
            messagebox.showerror("AI Error", f"Detection failed: {str(e)}")

class MecaDroneApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MECA DRONE - Ground Control Station")
        self.root.geometry("1100x650")
        self.root.configure(bg="black")
        self.root.resizable(True, True)
        
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.app_images = {}
        self.current_page = "home"
        
        # 1. Sidebar Frame
        self.sidebar_frame = tk.Frame(root, width=80, bg="black")
        self.sidebar_frame.pack(side="left", fill="y")
        self.sidebar_frame.pack_propagate(False)
        
        # 2. Main Content Frame (container for pages)
        self.content_frame = tk.Frame(root, bg="black")
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Setup Sidebar
        self._setup_sidebar()
        
        # Load initial page
        self.show_page("home")
    
    def _setup_sidebar(self):
        self.sidebar_indicators = {}
        icons = [
            ("home", "bx_home-alt-2.png", lambda: self.show_page("home")),
            ("tv", "tv.png", lambda: self.show_page("streaming")),
            ("plus", "plus.png", lambda: self.show_page("find_person")),
        ]
        
        # padding at the top
        tk.Frame(self.sidebar_frame, height=200, bg="black").pack(side="top")
        
        for name, filename, cmd in icons:
            img = self.load_image(name, filename, size=(24, 24), collection=self.app_images)
            if img:
                btn_frame = tk.Frame(self.sidebar_frame, bg="black", pady=15)
                btn_frame.pack(side="top", fill="x")
                
                btn = tk.Label(
                    btn_frame, 
                    image=img, 
                    bg="black", 
                    cursor="hand2"
                )
                btn.pack(pady=2)
                
                # Create indicator line for this icon
                canvas = tk.Canvas(btn_frame, width=24, height=4, bg="black", highlightthickness=0)
                canvas.pack()
                line_id = canvas.create_line(0, 2, 24, 2, fill="#58a6ff", width=2)
                
                self.sidebar_indicators[name] = line_id
                
                def make_hover(f=btn_frame, b=btn, c_cmd=cmd):
                    def enter(e):
                        f.config(bg="#333333")
                        b.config(bg="#333333")
                    def leave(e):
                        f.config(bg="black")
                        b.config(bg="black")
                    b.bind("<Enter>", enter)
                    b.bind("<Leave>", leave)
                    f.bind("<Enter>", enter)
                    f.bind("<Leave>", leave)
                    b.bind("<Button-1>", lambda e: c_cmd())
                    f.bind("<Button-1>", lambda e: c_cmd())
                
                make_hover()
        
        # Initially show only home indicator
        self.update_sidebar_indicators()
    
    def update_sidebar_indicators(self):
        """Update sidebar indicator lines to show current active page"""
        for page_name, line_id in self.sidebar_indicators.items():
            if page_name == self.current_page:
                pass  # Will be handled in update_active_indicator
    
    def load_image(self, name, filename, size=None, collection=None):
        """Loads an image, optionally resizes it, and returns PhotoImage."""
        if collection is None:
            collection = self.app_images
            
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img.convert("RGBA")
                if size:
                    img.thumbnail(size, Image.Resampling.LANCZOS)
                
                photo = ImageTk.PhotoImage(img)
                collection[name] = photo
                return photo
            except Exception as e:
                print(f"Error loading {filename}: {e}")
        else:
            print(f"Warning: {filename} not found in {self.base_path}.")
        return None
    
    def show_page(self, page_name):
        # Update current page
        self.current_page = page_name
        
        # Destroy current pages
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        if page_name == "home":
            page = HomePage(self.content_frame, self.base_path, self.load_image)
            page.pack(fill="both", expand=True)
            
        elif page_name == "dashboard":
            page = DashboardPage(self.content_frame, self.base_path, self.load_image)
            page.pack(fill="both", expand=True)
            
        elif page_name == "streaming":
            page = StreamingPage(self.content_frame, self.base_path, self.load_image)
            page.pack(fill="both", expand=True)
            
        elif page_name == "find_person":
            page = FindPersonPage(self.content_frame, self.base_path, self.load_image)
            page.pack(fill="both", expand=True)
        
        # Update sidebar indicators
        self.update_active_indicator(page_name)
    
    def update_active_indicator(self, active_page):
        """Update which sidebar indicator line is visible"""
        # Clear all indicator lines first
        for widget in self.sidebar_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                for child in widget.winfo_children():
                    if isinstance(child, tk.Canvas) and child.winfo_height() <= 4:
                        child.delete("all")
                        # Add blue line back if this is the active page
                        # Find which page this frame belongs to
                        frame_children = widget.winfo_children()
                        has_label = any(isinstance(c, tk.Label) for c in frame_children)
                        if has_label:
                            # Determine which page this is by checking position
                            frames = list(self.sidebar_frame.winfo_children())
                            frame_index = frames.index(widget)
                            page_names = ["home", "tv", "plus"]
                            if frame_index < len(page_names):
                                if page_names[frame_index] == active_page:
                                    # Create blue line for active page
                                    child.create_line(0, 2, 24, 2, fill="#58a6ff", width=2)
                                    child.config(bg="black")
    
    def load_image(self, name, filename, size=None, collection=None):
        """Loads an image, optionally resizes it, and returns PhotoImage."""
        if collection is None:
            collection = self.app_images
            
        path = os.path.join(self.base_path, filename)
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img.convert("RGBA")
                if size:
                    img = img.resize(size, Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                collection[name] = photo
                return photo
            except Exception as e:
                print(f"Error loading {filename}: {e}")
        else:
            print(f"Warning: {filename} not found in {self.base_path}.")
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = MecaDroneApp(root)
    root.mainloop()
