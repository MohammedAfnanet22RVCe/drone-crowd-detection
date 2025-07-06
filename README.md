# Drone-Based Real-Time Crowd Detection and Alert System

This project implements a **real-time crowd detection and alert system** using a drone camera feed. The system utilizes **YOLOv8** for object detection, **OpenCV** for video processing, and **Flask** to host a local alert webpage. It counts people from live video streamed via a mobile phone using **scrcpy**, and raises an alert if the number of detected persons exceeds a user-defined threshold.

---

## 🔍 Features

- ✅ Real-time object detection using [YOLOv8](w)
- ✅ Person counting from live video feed
- ✅ Live screen capture via [mss](w)
- ✅ User-defined crowd threshold
- ✅ Web-based alert system using [Flask](w)
- ✅ Mobile compatibility using [scrcpy](w) and [ngrok](w)
- ✅ Local desktop notifications with [Plyer](w)
- ✅ Compatible with drone camera apps like **WiFi UAV**

---

## 🛠 Technologies Used

- [YOLOv8](w)
- [OpenCV](w)
- [Flask](w)
- [mss](w)
- [scrcpy](w)
- [ngrok](w)
- [plyer](w)

---
## 📸 Architecture Overview

Drone Camera → Mobile App (WiFi UAV) → scrcpy (PC) → YOLOv8 Detection → Crowd Count → Alert (Web + Console)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/drone-crowd-detection.git
cd drone-crowd-detection
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Launch the web alert server

```bash
python webserver.py
```

Web server will run on http://localhost:5000

Use ngrok to expose it over the internet:
```bash
ngrok http 5000
```

### 4. Run the Detection Script
```python
python maidet.py
```
### 5. Mobile Setup
Install scrcpy and connect your phone via USB to mirror the drone camera app (e.g., WiFi UAV).

Adjust monitor_region in detect_screen.py to match the scrcpy window position.

### 6. Configuration

In detect_screen.py:
```python
monitor_region = {"top": 100, "left": 100, "width": 640, "height": 480}
threshold = int(input("Enter crowd threshold: "))
```
Adjust these based on your screen and crowd threshold preference.

### ✍️ Authors

- **Mohammed Afnan**  
  6th Sem, ETE, RVCE – [GitHub](https://github.com/MohammedAfnanet22RVCe) [LinkedIn](https://www.linkedin.com/in/mohammed-afnan-17b30122a/)

### 👥 Collaborators

- **Karunesh Kumar**  
  6th Sem, IEM, RVCE – [GitHub](https://github.com/Karunesh3770)

- **Rahul Chatterjee**  
  6th Sem, EIE, RVCE

- **Harsh Raj**  
  6th Sem, ASE, RVCE

- **Avneesh Singh**  
  6th Sem, CSE, RVCE

- **Advith Padyana**  
  6th Sem, ISE, RVCE – [GitHub](http://github.com/advith15)

