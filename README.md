<div align="center">

# 🤖 ScoutBot — Autonomous Surveillance Robot

**Real-time intrusion detection · License plate recognition · Autonomous navigation**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-4B-C51A4A?style=flat-square&logo=raspberry-pi&logoColor=white)](https://raspberrypi.org)
[![Firebase](https://img.shields.io/badge/Firebase-Realtime_DB-FFCA28?style=flat-square&logo=firebase&logoColor=black)](https://firebase.google.com)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)](LICENSE)

> An autonomous surveillance robot that patrols restricted areas, detects intruders and unauthorized vehicles in real-time, and streams live feeds to a web dashboard — all on a Raspberry Pi 4.

![ScoutBot Dashboard](https://github.com/user-attachments/assets/325612a7-ce66-427c-b7ee-037496280588)

</div>

---

## 📌 The Problem It Solves

Manual surveillance of restricted workplaces and private parking lots is expensive, inconsistent, and reactive. Security guards miss events; static cameras have blind spots and require human monitoring.

**ScoutBot** replaces passive monitoring with an active, autonomous agent that:
- Patrols on a predefined map without human intervention
- Detects and identifies threats in real-time using computer vision
- Immediately alerts stakeholders and logs evidence to the cloud

---

## ✨ Key Features

| Feature | Detail |
|---|---|
| 🧠 **Face Recognition** | Identifies registered vs. unregistered individuals using OpenCV; ~90% accuracy in controlled environments |
| 🚗 **License Plate OCR** | Reads plates in real-time using EasyOCR; cross-checks against a registered vehicle database |
| 🗺️ **Autonomous Navigation** | Follows a predefined map, performs obstacle avoidance via HC-SR04 ultrasonic + servo sweep |
| 📡 **Live Video Streaming** | Streams RPi Camera Module 2 feed to a web dashboard over MQTT/HTTP |
| 🔔 **Real-time Alerts** | Push notifications to dashboard on unauthorized detection via Firebase |
| 🎛️ **Three Operating Modes** | Workplace Intrusion · Parking Surveillance · Live Stream |

---

## 🎬 System Demo

> *(Insert GIF or demo video link here — even a 20-second screen recording improves profile views by 3×)*

**Algorithm Flow:**

![Algorithm Flow](https://github.com/user-attachments/assets/bed5caf8-1d52-4f3a-90ef-bed304c5a803)

**Physical Robot:**

![ScoutBot Physical](https://github.com/user-attachments/assets/e3ddc373-ba05-47d9-b057-11a2a5bfd951)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────┐
│                   ScoutBot Robot                    │
│                                                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────────┐  │
│  │ RPi Cam  │───▶│  OpenCV  │───▶│ Face / Plate │  │
│  │ Module 2 │    │ Pipeline │    │  Classifier  │  │
│  └──────────┘    └──────────┘    └──────┬───────┘  │
│                                         │           │
│  ┌──────────┐    ┌──────────┐           ▼           │
│  │ HC-SR04  │───▶│Obstacle  │    ┌──────────────┐  │
│  │Ultrasonic│    │Avoidance │    │   Firebase   │  │
│  └──────────┘    └────┬─────┘    │ Realtime DB  │  │
│                       │          └──────┬───────┘  │
│  ┌──────────┐    ┌────▼─────┐          │           │
│  │  L298N   │◀───│ Motor    │          │           │
│  │  Driver  │    │ Control  │          │           │
│  └──────────┘    └──────────┘          │           │
└─────────────────────────────────────────┼───────────┘
                                          │ MQTT / HTTP
                              ┌───────────▼───────────┐
                              │     Web Dashboard      │
                              │  (Live Feed + Alerts)  │
                              └───────────────────────┘
```

---

## ⚙️ Hardware

### Bill of Materials

| Component | Model | Role |
|---|---|---|
| Single-Board Computer | Raspberry Pi 4 (4GB) | Main compute unit |
| Camera | RPi Camera Module 2 (MIPI CSI) | Vision input |
| Motor Driver | L298N | Dual DC motor control |
| DC Motors | 2× TT Gear Motors | Differential drive |
| Servo Motor | SG90 | Ultrasonic sensor pan |
| Ultrasonic Sensor | HC-SR04 | Obstacle detection |
| Power Regulator | Buck Converter | 5V regulated output for Pi |
| Power Source | 7.4V–12V Li-ion/LiPo | Main battery pack |

### Wiring Reference

<details>
<summary><strong>🔌 Click to expand full wiring table</strong></summary>

#### Power
| Supply | Connection |
|---|---|
| Buck Converter Input | Main battery (7.4V–12V) |
| Buck Converter Output | 5V → Raspberry Pi 4 |
| L298N Vcc | Direct from battery (motor power) |
| Ground | Common — Pi, L298N, servo, ultrasonic, battery |

#### DC Motors via L298N
| L298N Pin | GPIO |
|---|---|
| ENA | GPIO18 (PWM) |
| IN1 / IN2 | GPIO23 / GPIO24 |
| ENB | GPIO19 (PWM) |
| IN3 / IN4 | GPIO27 / GPIO22 |

#### Ultrasonic Sensor (HC-SR04)
| HC-SR04 Pin | GPIO |
|---|---|
| Trig | GPIO17 |
| Echo | GPIO27 ⚠️ via voltage divider (5V→3.3V) |

#### Servo Motor
| Servo Pin | GPIO |
|---|---|
| Signal | GPIO12 (PWM) |

#### Camera
| Module | Connection |
|---|---|
| RPi Camera Module 2 | CSI port on Raspberry Pi 4 |

</details>

---

## 💻 Software Stack

```
Computer Vision    →  Python · OpenCV · EasyOCR
Connectivity       →  MQTT · HTTP · Firebase Realtime DB
Web Dashboard      →  HTML · CSS · Tailwind · JavaScript
Hardware Control   →  RPi.GPIO · pigpio
```

---

## 🚀 Getting Started

### Prerequisites

- Raspberry Pi 4 running Raspberry Pi OS (64-bit recommended)
- Python 3.10+
- RPi Camera Module 2 enabled via `raspi-config`

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ScoutBot.git
cd ScoutBot

# Install Python dependencies
pip install -r requirements.txt

# Configure Firebase credentials
cp config/firebase_config.example.json config/firebase_config.json
# → Add your Firebase project credentials
```

### Running ScoutBot

```bash
# Workplace Intrusion Mode
python main.py --mode workplace

# Parking Surveillance Mode
python main.py --mode parking

# Live Stream Mode
python main.py --mode stream
```

---

## 📁 Project Structure

```
ScoutBot/
├── main.py                  # Entry point — mode selector
├── modes/
│   ├── workplace.py         # Face recognition pipeline
│   ├── parking.py           # License plate OCR pipeline
│   └── livestream.py        # Camera streaming handler
├── navigation/
│   ├── motor_control.py     # L298N PWM control
│   ├── obstacle_avoidance.py# HC-SR04 + servo sweep logic
│   └── path_follower.py     # Predefined map navigation
├── vision/
│   ├── face_recognition.py  # OpenCV face detect + match
│   └── plate_ocr.py         # EasyOCR license plate reader
├── dashboard/               # Web frontend (HTML/Tailwind/JS)
├── config/                  # Firebase & system config
└── requirements.txt
```

---

## 📊 Performance Results

| Metric | Result |
|---|---|
| Face detection accuracy | ~90% (controlled indoor environment) |
| License plate read rate | ~90% (clear lighting, <2m distance) |
| Obstacle avoidance clearance | Zero collisions across structured test runs |
| Alert latency (detection → notification) | < 2 seconds over local WiFi |

---

## 🗺️ Roadmap

- [ ] SLAM-based dynamic mapping (replace predefined path)
- [ ] Night vision support (IR camera module)
- [ ] Multi-robot coordination
- [ ] Edge TPU acceleration for on-device inference
- [ ] Mobile app for push notifications

---

## 👤 Author

**Aaishwarya Sheth** — Embedded Engineer | Robotics | Firmware  
[LinkedIn](https://linkedin.com/in/yourprofile) · [GitHub](https://github.com/yourusername) · [Email](mailto:aaishwarya.sheth@gmail.com)

> *If this project helped you or you found it interesting, a ⭐ on the repo goes a long way!*

---

<div align="center">
  <sub>Built with Raspberry Pi 4 · OpenCV · Firebase · Python</sub>
</div>
