# ScoutBot-Autonomous Surveillance Robot

## Purpose
ScoutBot is a surveillance robot concept designed for restricted workplaces and private parking areas.
 - In workplaces, it ensures security by detecting intrusions and monitoring access.
 - In private parking, it identifies unauthorized vehicles and alerts the user.
 - It can also provide live video streaming for real-time monitoring.

## Working
**User selects the usage mode**:
 - Workplace Mode – Detects intruders’ faces and streams the feed to a website.
 - Parking Mode – Detects unauthorized vehicles parked in the area and sends a notification.
 - Live Stream Mode – Provides continuous video streaming.

**The robot**:
 - Navigates autonomously using a predefined mapped feed.
 - Performs obstacle avoidance to ensure safe movement.
 - Sends real-time alerts/feeds to a connected website.

## Technologies Used
### Hardware: 
 - RaspberryPi 4
 - Cam module 2
 - 2 DC motor
 - Buck Convertor
 - L298N Driver
 - Servo Motor
 - HC-SR04
   
#### Wiring Connections – Surveillance Bot  

**Power Connections**
| Pin / Supply | Connection |
|--------------|------------|
| Buck Converter Input | Main battery pack (e.g., 7.4V–12V Li-ion/LiPo) |
| Buck Converter Output | 5V regulated → powers Raspberry Pi 4 |
| L298N Vcc (12V pin)   | Direct from main battery (for DC motors) |
| Ground                | Common ground between Pi, L298N, servo, ultrasonic, and battery |


**DC Motors (M1, M2) – L298N Driver**
| L298N Pin | Raspberry Pi GPIO / Connection |
|-----------|--------------------------------|
| ENA       | GPIO18 (PWM) |
| IN1       | GPIO23 |
| IN2       | GPIO24 |
| OUT1, OUT2| DC Motor 1 terminals |
| ENB       | GPIO19 (PWM) |
| IN3       | GPIO27 |
| IN4       | GPIO22 |
| OUT3, OUT4| DC Motor 2 terminals |
| Vcc (12V) | Battery + |
| GND       | Common ground |


**Ultrasonic Sensor (HC-SR04)** 
| HC-SR04 Pin | Raspberry Pi GPIO |
|-------------|-------------------|
| Vcc         | 5V |
| GND         | GND |
| Trig        | GPIO17 |
| Echo        | GPIO27 (use voltage divider to step down to 3.3V) |


**Servo Motor (Ultrasonic Mount)**
| Servo Pin  | Raspberry Pi GPIO |
|------------|-------------------|
| Vcc        | 5V (from buck converter / Pi 5V pin, with enough current) |
| GND        | Common ground |
| Signal     | GPIO12 (PWM) |


**Camera Module**
| Camera | Connection |
|--------|-------------|
| RPi Camera Module 2 | CSI port on Raspberry Pi 4 |

### Software:
  - Python, OpenCV, EasyOCR
  - MicroPython (for Pico W)
  - Firebase 
  - MQTT / HTTP
    
## Prototype: 
**Dashboard** 
<img width="1920" height="1044" alt="Screenshot 2025-06-26 154945" src="https://github.com/user-attachments/assets/325612a7-ce66-427c-b7ee-037496280588" />
**Algorithm Flow**
<img width="1306" height="844" alt="image" src="https://github.com/user-attachments/assets/bed5caf8-1d52-4f3a-90ef-bed304c5a803" />

**ScoutBot** 



