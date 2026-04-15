# ⚙️ Backend - Rust Services

## 📁 **Location:** `backend/`

## 🎯 **Overview**
Rust-based backend services for MECA DRONE system using Tauri framework for desktop integration.

## 🚀 **Backend Services**

### **Core Services:**
- **Telemetry Bridge** - MAVLink protocol handling
- **Command Processing** - Emergency and navigation commands
- **Data Management** - Telemetry storage and retrieval
- **Communication** - UDP and HTTP server functionality

### **Technology Stack:**
- **Rust** - Systems programming language
- **Tauri** - Desktop app framework
- **Tokio** - Async runtime
- **Serde** - Serialization/deserialization
- **MAVLink** - Drone communication protocol (planned)

## 📡 **Communication Protocols**

### **UDP Telemetry:**
- **Port**: 14550
- **Protocol**: MAVLink
- **Purpose**: Real-time telemetry from drone
- **Status**: Ready for integration

### **HTTP Server:**
- **Port**: 5000
- **Purpose**: Target image uploads
- **Endpoints**: `/upload` for image processing
- **Status**: Mock implementation ready

### **Tauri Commands:**
- `get_telemetry()` - Retrieve telemetry data
- `emergency_land()` - Send emergency landing command
- `kill_switch()` - Send kill switch command
- `upload_target()` - Upload target image
- `test_connection()` - Test drone connectivity

## 🔧 **Project Structure**

```
backend/
└── src-tauri/
    ├── src/
    │   └── main.rs          # Main backend logic
    ├── Cargo.toml           # Rust dependencies
    ├── tauri.conf.json      # Tauri configuration
    └── build.rs             # Build script
```

## 📊 **Data Structures**

### **TelemetryData:**
```rust
pub struct TelemetryData {
    pub altitude: f64,
    pub battery_voltage: f64,
    pub gps_lock: bool,
    pub connection_strength: i32,
    pub latitude: f64,
    pub longitude: f64,
    pub speed: f64,
    pub heading: f64,
    pub timestamp: u64,
}
```

### **Current Implementation:**
- **Mock data generation** for testing
- **Real-time updates** at 10Hz
- **Error handling** with Result types
- **Async operations** for non-blocking I/O

## 🚀 **Build and Run**

### **Prerequisites:**
- **Rust toolchain** installed
- **Tauri CLI** available

### **Development:**
```bash
cd src-tauri
cargo run
```

### **Production Build:**
```bash
cd src-tauri
cargo build --release
```

### **Tauri Build:**
```bash
cd src-tauri
cargo tauri build
```

## 🔗 **Integration Points**

### **Frontend Connection:**
- **Tauri commands** for frontend-backend communication
- **Real-time data streaming**
- **Event-driven architecture**

### **Hardware Integration:**
- **Raspberry Pi** connection
- **MAVLink protocol** implementation
- **Serial communication** with drone hardware

### **AI Integration:**
- **Person detection** results processing
- **Target tracking** data
- **Autonomous navigation** commands

## 📋 **Current Features**

### ✅ **Implemented:**
- **Mock telemetry** data generation
- **Tauri command** structure
- **Emergency controls** handling
- **Image upload** simulation
- **Connection testing** functionality

### 🔄 **Ready for Integration:**
- **Real MAVLink** telemetry
- **Hardware communication**
- **Video streaming** support
- **AI processing** integration

## 🛠️ **Dependencies**

### **Core Dependencies:**
```toml
[dependencies]
tauri = { version = "2.0", features = ["shell-open"] }
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1.0", features = ["full"] }
```

### **Planned Dependencies:**
- **mavlink** - MAVLink protocol parsing
- **opencv** - Computer vision integration
- **reqwest** - HTTP client functionality
- **serialport** - Hardware communication

## 🔒 **Security**

### **Current Measures:**
- **Input validation** for all commands
- **Error handling** with proper types
- **Safe Rust** practices

### **Planned Enhancements:**
- **Authentication** for drone access
- **Encryption** for communication
- **Access control** for commands

## 🚀 **Future Development**

### **Phase 1: Hardware Integration**
- **MAVLink implementation**
- **Serial communication**
- **Real telemetry processing**

### **Phase 2: Advanced Features**
- **Video streaming** server
- **Data logging** system
- **Performance monitoring**

### **Phase 3: AI Integration**
- **Person detection** processing
- **Autonomous navigation**
- **Advanced analytics**

---

**Ready for professional drone backend services!** 🚁✨
