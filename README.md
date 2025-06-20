# ScoutBot-Autonomous Surveillance Robot
ScoutBot is designed for intrusion detection and private parking monitoring using computer vision , IoT, and real-time alert.

# Purpose
To develop a smart, mobile robot that can:
- Detect unauthorized human activity in restricted workplace zones.
- Monitor private parking areas for unauthorized vehicles using license plate recognition.

# Working
ScoutBot begins by connecting to Wi-Fi and loading a pre-mapped layout.It starts autonomous patrolling using obstacle avoidance and real-time sensors.A camera captures live video, processed using OpenCV for human or vehicle detection.In intrusion mode, it identifies unauthorized people and sends alerts with images.In parking mode, it uses OCR to read number plates and matches them with a database.Unrecognized plates or misuse of parking space trigger alerts.All alerts, images, and logs are sent to a cloud dashboard or mobile app.MicroPython handles lightweight sensor data; Python manages camera.The system operates independently, adapting to environment changes dynamically.This allows secure, real-time surveillance with minimal human involvement.

## Technologies Used
- **Hardware**: Raspberry Pi Zero 2 W, Ultrasonic Sensor HC-SR04, Motor Driver L298N, Camera Module 2.
- **Software**:
  - Python, OpenCV, EasyOCR
  - MicroPython (for Pico W)
  - Firebase / Cloud DB
  - MQTT / HTTP


