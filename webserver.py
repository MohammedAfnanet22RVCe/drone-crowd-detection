from flask import Flask, render_template_string

app = Flask(__name__)

# Shared data
current_status = {
    "status": "SAFE",
    "count": 0,
    "threshold": 0
}

# HTML Template
HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Crowd Status Monitor</title>
    <meta http-equiv="refresh" content="3">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background-color: #f5f5f5;
            text-align: center;
            padding-top: 80px;
        }
        .status {
            font-size: 3em;
            font-weight: bold;
            color: {{ 'green' if status == 'SAFE' else 'red' }};
        }
        .info {
            font-size: 1.5em;
            margin-top: 20px;
        }
        .emoji {
            font-size: 5em;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="emoji">
        {% if status == 'SAFE' %}
            🟢
        {% else %}
            🔴
        {% endif %}
    </div>
    <div class="status">{{ status }}</div>
    <div class="info">
        👥 People Detected: <b>{{ count }}</b><br>
        ⚠️ Threshold Limit: <b>{{ threshold }}</b>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(
        HTML,
        status=current_status["status"],
        count=current_status["count"],
        threshold=current_status["threshold"]
    )

# Function for detector to update status
def update_status(new_status, count=0, threshold=0):
    current_status["status"] = new_status
    current_status["count"] = count
    current_status["threshold"] = threshold

# Start the server in a thread (call from detector)
from threading import Thread
def start_server():
    app.run(host='0.0.0.0', port=5000)

# Launch Flask server in a background thread
Thread(target=start_server).start()
