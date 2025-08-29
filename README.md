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
| Component           | Connections                 |
|---------------------|-----------------------------|
| Raspberry Pi Zero 2W|                             |
| Pi Camera Module 2  |                             |
| HC-SR04             |                             |
| L298N Motor Driver  |                             |

**Software**:
  - Python, OpenCV, EasyOCR
  - MicroPython (for Pico W)
  - Firebase 
  - MQTT / HTTP
    
## Prototype: 
**Dashboard** 
<img width="1920" height="1044" alt="Screenshot 2025-06-26 154945" src="https://github.com/user-attachments/assets/325612a7-ce66-427c-b7ee-037496280588" />

**ScoutBot** 



