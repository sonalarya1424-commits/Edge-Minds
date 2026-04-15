import requests
import time
import random

URL = "http://127.0.0.1:5000/predict"

def generate_data():
    return {
        "vibration": random.uniform(0, 10),
        "temperature": random.uniform(20, 100),
        "pressure": random.uniform(1, 10),
        "voltage": random.uniform(200, 600),
        "current": random.uniform(1, 50),
        "rpm": random.uniform(50, 2000),
        "network_delay": random.uniform(1, 200),
        "device_id": 1,
        "sound": random.uniform(20, 100),
        "humidity": random.uniform(20, 90)
    }

print(" Auto Simulation Started...\n")

while True:
    try:
        data = generate_data()

        response = requests.post(URL, json=data)
        result = response.json()

        print(" DATA:", data)
        print(" Prediction:", result.get("prediction"))
        print(" Cyber:", result.get("attack"))
        print("-" * 50)

        time.sleep(10)  # Every 10 seconds

    except Exception as e:
        print(" Error:", e)
        time.sleep(5)