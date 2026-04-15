# 🚁 MECA DRONE - Ground Control Station

## 📁 **Project Structure**

```
MECA DRONE/
├── frontend/           # Desktop Application (Python/Tkinter)
├── backend/            # Rust Backend (Tauri/Rust)
├── ai/                 # AI Person Detection (Coming Soon)
└── README.md           # This file
```

## 🎯 **Desktop Application Only**

This project has been cleaned up to contain **ONLY the desktop version** - all web-related files have been removed.

---

## 🖥️ **Frontend (Desktop Application)**

### **Location:** `frontend/`

### **Technology Stack:**
- **Python 3** with **Tkinter** for native desktop UI
- **Real-time telemetry** updates (10Hz)
- **Dark tactical interface** matching MECA DRONE branding
- **Native Windows application** (not browser-based)

### **Files:**
- `meca-drone.py` - Main desktop application
- `MECA-DRONE-Native-Desktop.bat` - Launcher script
- `hero.png` - MECA DRONE branding image
- `desktop-app.html` - HTML fallback version
- `MECA-DRONE-Window.html` - Enhanced HTML version

### **Features:**
- ✅ **Real-time telemetry dashboard**
- ✅ **Emergency controls** (Land Now, Kill Switch)
- ✅ **Navigation system** (Home, Dashboard, Video, Upload, Settings)
- ✅ **Professional dark UI** with amber accents
- ✅ **Desktop integration** (shortcuts, taskbar)

### **Launch:**
```bash
# From project root
python frontend/meca-drone.py

# Or use the launcher
frontend/MECA-DRONE-Native-Desktop.bat
```

---

## ⚙️ **Backend (Rust Services)**

### **Location:** `backend/`

### **Technology Stack:**
- **Rust** with **Tauri** framework
- **MAVLink protocol** support (ready for integration)
- **UDP communication** on port 14550
- **HTTP server** for image uploads (port 5000)

### **Current Features:**
- ✅ **Mock telemetry data generator**
- ✅ **Tauri commands** for frontend communication
- ✅ **Emergency command handling**
- ✅ **Target image upload simulation**
- ✅ **Connection testing**

### **Ready for Integration:**
- **Real drone telemetry** (MAVLink)
- **Hardware communication** (Raspberry Pi)
- **Video streaming** (WebRTC/RTSP)
- **Person detection** (AI integration)

---

## 🤖 **AI Person Detection**

### **Location:** `ai/`

### **✅ NOW AVAILABLE:**
- **Person Detection System** - YOLO + DeepFace integration
- **Real-time Tracking** - Target identification and following
- **Desktop Integration** - Connected to main application
- **Raspberry Pi Ready** - Optimized for drone deployment

### **Features:**
- **YOLOv8/YOLOv26** for person detection
- **DeepFace** for facial recognition
- **Target matching** with confidence scoring
- **Performance optimized** for embedded systems
- **Hardware documentation** included

### **Files:**
- `person_detection.py` - Main detection system
- `drone_detection_optimized.py` - Raspberry Pi version
- `integration.py` - Desktop app integration
- `requirements.txt` - Python dependencies
- `best.pt`, `yolo26n` - AI model weights
- `hardware/` - Hardware documentation and pinouts

### **Usage:**
```bash
# Install dependencies
pip install -r ai/requirements.txt

# Run desktop version
python ai/person_detection.py

# Run optimized version (Raspberry Pi)
python ai/drone_detection_optimized.py
```

### **Integration:**
- **Desktop App**: Connected via integration module
- **Backend**: Ready for Rust service communication
- **Hardware**: UART communication documentation included

### **Prerequisites:**
- **Python 3** installed on system
- **Rust toolchain** (for backend development)

---

## 🚀 **Getting Started**

### **Prerequisites:**
- **Python 3** installed on system
- **Rust toolchain** (for backend development)

### **Quick Start:**
1. **Launch Desktop App:**
   ```bash
   python frontend/meca-drone.py
   ```

2. **Navigate the Interface:**
   - **Home** - Welcome screen with MECA DRONE branding
   - **Dashboard** - Real-time telemetry monitoring
   - **Video** - Live video stream (ready for integration)
   - **Upload** - Target image upload (ready for integration)
   - **Settings** - Configuration panel

### **Desktop Integration:**
- **Desktop shortcut** created automatically
- **Native Windows application**
- **Professional desktop experience**

---

## 🔧 **Development**

### **Frontend Development:**
```bash
# Run desktop app
python frontend/meca-drone.py

# Edit the main file
frontend/meca-drone.py
```

### **Backend Development:**
```bash
# Navigate to backend
cd backend/src-tauri

# Build backend
cargo build

# Run backend
cargo run
```

### **AI Integration:**
```bash
# AI components will be added here
# Person detection code will be integrated
```

---

## 📊 **Current Status**

### **✅ Completed:**
- **Desktop application** with full UI
- **Real-time telemetry** simulation
- **Emergency controls** and safety features
- **Professional dark interface**
- **Project structure** cleanup

### **🔄 Ready for Integration:**
- **Real drone hardware** (Raspberry Pi)
- **MAVLink telemetry** (UDP 14550)
- **Video streaming** (WebRTC/RTSP)
- **Person detection** (AI integration)

### **📋 Next Steps:**
1. **Add AI person detection** code
2. **Integrate real drone hardware**
3. **Connect MAVLink telemetry**
4. **Setup video streaming**

---

## 🎯 **Desktop Application Features**

### **Telemetry Dashboard:**
- **Altitude** monitoring in meters
- **Battery voltage** with color coding
- **GPS lock** status with coordinates
- **Signal strength** percentage
- **Connection status** indicator

### **Emergency Controls:**
- **Land Now** - Safe emergency landing
- **Kill Switch** - Immediate motor stop (with confirmation)

### **Navigation System:**
- **Sidebar navigation** with icons
- **Page transitions** with animations
- **Active state indicators**
- **Hover effects**

### **Professional UI:**
- **Dark tactical theme**
- **Amber accent colors**
- **Glass morphism effects**
- **Smooth animations**

---

## 🚁 **MECA DRONE Mission**

This desktop Ground Control Station provides:
- **Professional drone control** interface
- **Real-time monitoring** capabilities
- **Emergency response** systems
- **AI-powered person detection** (coming soon)
- **Hardware integration** ready

**Built for professional drone operations with safety and reliability in mind.**
