import cv2
import numpy as np
import mss
import mss.tools
from ultralytics import YOLO
from plyer import notification  # 🆕 Notification module

model = YOLO('yolov8s.pt')

# Set your desired screen region (adjust as per scrcpy window position)
monitor_region = {"top": 100, "left": 100, "width": 640, "height": 480}

# Ask for threshold
threshold = int(input("Enter crowd threshold to trigger alert: "))

alert_sent = False  # To prevent repeated notifications

with mss.mss() as sct:
    while True:
        screenshot = sct.grab(monitor_region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        
        results = model.predict(frame, conf=0.3)[0]

        person_count = 0
        for box in results.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label == 'person':
                person_count += 1
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(frame, f"{label} {box.conf[0]:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Set status and color
        status = "TOO CROWDED" if person_count > threshold else "SAFE"
        color = (0, 0, 255) if status == "TOO CROWDED" else (0, 255, 0)

        # Show count + status on screen
        cv2.putText(frame, f"People Count: {person_count} | Status: {status}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # 🔔 Trigger notification only once when threshold is crossed
        if person_count > threshold:
            if not alert_sent:
                notification.notify(
                    title="🚨 Crowd Alert",
                    message=f"Too many people detected: {person_count}",
                    timeout=5
                )
                alert_sent = True
        else:
            alert_sent = False  # Reset when safe

        cv2.imshow("Drone Feed Crowd Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.destroyAllWindows()
