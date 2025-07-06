import cv2
import numpy as np
import mss
import mss.tools
from ultralytics import YOLO
from plyer import notification
import webserver  # <-- Your web status server module

model = YOLO('yolov8s.pt')

# Adjust this to your scrcpy window position
monitor_region = {"top": 100, "left": 100, "width": 640, "height": 480}

# Set crowd threshold
threshold = int(input("Enter crowd threshold to trigger alert: "))
alert_sent = False  # To avoid spamming notifications

with mss.mss() as sct:
    while True:
        # Capture screen
        screenshot = sct.grab(monitor_region)
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # Run YOLO prediction
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

        # Status and color for display
        status = "TOO CROWDED" if person_count > threshold else "SAFE"
        color = (0, 0, 255) if status == "TOO CROWDED" else (0, 255, 0)

        # Show count + status on screen
        cv2.putText(frame, f"People Count: {person_count} | Status: {status}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        # 🔔 Desktop Notification
        if status == "TOO CROWDED":
            if not alert_sent:
                notification.notify(
                    title="🚨 Crowd Alert",
                    message=f"Too many people detected: {person_count}",
                    timeout=5
                )
                alert_sent = True
        else:
            alert_sent = False  # Reset

        # 🌐 Update status on webserver
        webserver.update_status(status, person_count, threshold)


        # Show frame
        cv2.imshow("Drone Feed Crowd Detection", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.destroyAllWindows()
