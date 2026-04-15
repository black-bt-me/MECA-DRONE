// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use serde::{Deserialize, Serialize};
use std::collections::HashMap;
use std::time::{SystemTime, UNIX_EPOCH};

// Telemetry data structure
#[derive(Debug, Serialize, Deserialize, Clone)]
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

// Mock telemetry data generator
fn generate_mock_telemetry() -> TelemetryData {
    let timestamp = SystemTime::now()
        .duration_since(UNIX_EPOCH)
        .unwrap()
        .as_secs();
    
    TelemetryData {
        altitude: 50.0 + (timestamp % 100) as f64 * 0.5, // Varying altitude
        battery_voltage: 12.6 - (timestamp % 1000) as f64 * 0.001, // Slowly decreasing
        gps_lock: (timestamp % 2) == 0, // Alternating GPS lock
        connection_strength: 80 + (timestamp % 20) as i32, // Varying signal
        latitude: 37.7749 + (timestamp % 1000) as f64 * 0.0001, // Small variations
        longitude: -122.4194 + (timestamp % 1000) as f64 * 0.0001,
        speed: 15.0 + (timestamp % 50) as f64 * 0.2, // Varying speed
        heading: (timestamp % 360) as f64, // Rotating heading
        timestamp,
    }
}

// Tauri command to get telemetry data
#[tauri::command]
async fn get_telemetry() -> Result<TelemetryData, String> {
    // For now, return mock data
    // In the future, this will read from UDP port 14550 (MAVLink)
    let telemetry = generate_mock_telemetry();
    Ok(telemetry)
}

// Tauri command to send emergency land command
#[tauri::command]
async fn emergency_land() -> Result<String, String> {
    // Mock implementation - will send MAVLink command in the future
    println!("Emergency land command sent");
    Ok("Emergency land command sent successfully".to_string())
}

// Tauri command to send kill switch command
#[tauri::command]
async fn kill_switch() -> Result<String, String> {
    // Mock implementation - will send MAVLink command in the future
    println!("Kill switch command sent");
    Ok("Kill switch command sent successfully".to_string())
}

// Tauri command to upload target image
#[tauri::command]
async fn upload_target(drone_ip: String, image_data: Vec<u8>) -> Result<String, String> {
    // Mock implementation - will send HTTP POST to Flask server in the future
    println!("Uploading target image to drone at: {}", drone_ip);
    println!("Image size: {} bytes", image_data.len());
    
    // Simulate upload delay
    tokio::time::sleep(tokio::time::Duration::from_millis(1000)).await;
    
    Ok("Target image uploaded successfully".to_string())
}

// Tauri command to test drone connection
#[tauri::command]
async fn test_connection(drone_ip: String) -> Result<bool, String> {
    // Mock implementation - will ping the drone in the future
    println!("Testing connection to drone at: {}", drone_ip);
    
    // Simulate connection test
    tokio::time::sleep(tokio::time::Duration::from_millis(500)).await;
    
    // For now, always return true
    Ok(true)
}

fn main() {
    tauri::Builder::default()
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![
            get_telemetry,
            emergency_land,
            kill_switch,
            upload_target,
            test_connection
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
