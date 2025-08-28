# ScoutBot-Autonomous Surveillance Robot

# Purpose
ScoutBot is a surveillance robot concept designed for restricted workplaces and private parking areas.
 - In workplaces, it ensures security by detecting intrusions and monitoring access.
 - In private parking, it identifies unauthorized vehicles and alerts the user.
 - It can also provide live video streaming for real-time monitoring.

# Working
**User selects the usage mode**:
 - Workplace Mode – Detects intruders’ faces and streams the feed to a website.
 - Parking Mode – Detects unauthorized vehicles parked in the area and sends a notification.
 - Live Stream Mode – Provides continuous video streaming.

**The robot**:
 - Navigates autonomously using a predefined mapped feed.
 - Performs obstacle avoidance to ensure safe movement.
 - Sends real-time alerts/feeds to a connected website.

## Technologies Used
**Hardware**:
 - Raspberry Pi Zero 2 W, Ultrasonic Sensor HC-SR04, Motor Driver L298N, Camera Module 2.
**Software**:
  - Python, OpenCV, EasyOCR
  - MicroPython (for Pico W)
  - Firebase / Cloud DB
  - MQTT / HTTP


