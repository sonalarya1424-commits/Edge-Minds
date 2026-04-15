from flask import Flask, request, jsonify, send_file
import random

app = Flask(__name__)

# ===== AI + CYBERSECURITY LOGIC =====
def analyze_system(vibration, sound, temperature, rpm, network_delay):

    # ===== AI PREDICTION =====
    if vibration == 1 or sound > 600 or temperature > 50:
        prediction = " Anomaly Detected"
    else:
        prediction = " Normal"

    # ===== CYBERSECURITY ANALYSIS =====
    cyber_alerts = []

    # Sensor spoofing (RPM mismatch)
    if rpm < 300 and vibration == 1:
        cyber_alerts.append(" Possible Sensor Spoofing (RPM mismatch)")

    # MITM attack (network delay)
    if network_delay > 80:
        cyber_alerts.append(" Possible MITM Attack (High Network Delay)")

    # System tampering
    if temperature > 60 and sound < 200:
        cyber_alerts.append(" Possible System Tampering")

    if len(cyber_alerts) == 0:
        cyber_result = " No cyber threat detected"
    else:
        cyber_result = " | ".join(cyber_alerts)

    return prediction, cyber_result


# ===== HOME =====
@app.route('/')
def home():
    return send_file("frontend.html")


# ===== MANUAL PREDICT =====
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    try:
        vibration = float(data["vibration"])
        sound = float(data["sound"])
        temperature = float(data["temperature"])
        rpm = float(data["rpm"])
        network_delay = float(data["network_delay"])
    except:
        return jsonify({"result": "Fill required fields correctly"})

    prediction, cyber = analyze_system(vibration, sound, temperature, rpm, network_delay)

    return jsonify({
        "prediction": prediction,
        "cyber": cyber
    })


# ===== AUTO SIMULATION =====
@app.route('/simulate')
def simulate():

    # Core sensors
    vibration = random.choice([0, 1])
    sound = random.randint(200, 800)
    temperature = random.randint(25, 70)

    # Extra parameters
    pressure = random.randint(1, 10)
    voltage = random.randint(200, 250)
    current = random.uniform(0.5, 5.0)
    rpm = random.randint(100, 2000)
    network_delay = random.randint(1, 120)
    device_id = random.randint(1, 5)
    humidity = random.randint(30, 80)

    prediction, cyber = analyze_system(vibration, sound, temperature, rpm, network_delay)

    return jsonify({
        "vibration": vibration,
        "temperature": temperature,
        "pressure": pressure,
        "voltage": voltage,
        "current": round(current, 2),
        "rpm": rpm,
        "network_delay": network_delay,
        "device_id": device_id,
        "sound": sound,
        "humidity": humidity,
        "prediction": prediction,
        "cyber": cyber
    })


if __name__ == '__main__':
    app.run(debug=True)




from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


# from flask import Flask, request, jsonify
# import json
# import os
# from google import genai

# app = Flask(__name__)

# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

# client = genai.Client(api_key=api_key)

# @app.route("/generate_reports", methods=["POST"])
# def generate_reports():
#     try:
#         data = request.get_json()
#         prediction = data.get("prediction", "")
#         cyber = data.get("cyber", "")

#         prompt = f"""
# Write two separate reports in valid JSON only.

# Prediction input: {prediction}
# Cybersecurity input: {cyber}

# Return exactly:
# {{
#   "prediction_report": "around 50 words",
#   "cyber_report": "around 50 words"
# }}

# Keep both reports short, clear, and professional.
# """

#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=prompt
#         )

#         text = response.text.strip()

#         if text.startswith("```json"):
#             text = text.replace("```json", "").replace("```", "").strip()

#         result = json.loads(text)

#         return jsonify({
#             "prediction_report": result.get("prediction_report", "No prediction report generated."),
#             "cyber_report": result.get("cyber_report", "No cybersecurity report generated.")
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)
    

# from flask import Flask, request, jsonify
# import json
# import os
# from google import genai

# app = Flask(__name__)

# api_key = os.getenv("AIzaSyDYSYRAXZrZo-UptGdtS9SgFMjnlpim1E4")
# if not api_key:
#     raise ValueError("AIzaSyDYSYRAXZrZo-UptGdtS9SgFMjnlpim1E4 is not set in environment variables.")

# client = genai.Client(api_key=api_key)

# @app.route("/generate_reports", methods=["POST"])
# def generate_reports():
#     try:
#         data = request.get_json()
#         prediction = data.get("prediction", "")
#         cyber = data.get("cyber", "")

#         prompt = f"""
# Write two separate reports in valid JSON only.

# Prediction input: {prediction}
# Cybersecurity input: {cyber}

# Return exactly:
# {{
#   "prediction_report": "around 50 words",
#   "cyber_report": "around 50 words"
# }}

# Keep both reports short, clear, and professional.
# """

#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=prompt
#         )

#         text = response.text.strip()

#         if text.startswith("```json"):
#             text = text.replace("```json", "").replace("```", "").strip()

#         result = json.loads(text)

#         return jsonify({
#             "prediction_report": result.get("prediction_report", "No prediction report generated."),
#             "cyber_report": result.get("cyber_report", "No cybersecurity report generated.")
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import json
# import os
# from google import genai

# app = Flask(__name__)

# api_key = os.getenv("GOOGLE_API_KEY")
# if not api_key:
#     raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

# client = genai.Client(api_key=api_key)

# @app.route("/generate_reports", methods=["POST"])
# def generate_reports():
#     try:
#         data = request.get_json()
#         prediction = data.get("prediction", "")
#         cyber = data.get("cyber", "")

#         prompt = f"""
# Write two separate reports in valid JSON only.

# Prediction input: {prediction}
# Cybersecurity input: {cyber}

# Return exactly:
# {{
#   "prediction_report": "around 50 words",
#   "cyber_report": "around 50 words"
# }}

# Keep both reports short, clear, and professional.
# """

#         response = client.models.generate_content(
#             model="gemini-1.5-flash",
#             contents=prompt
#         )

#         text = response.text.strip()

#         if text.startswith("```json"):
#             text = text.replace("```json", "").replace("```", "").strip()

#         result = json.loads(text)

#         return jsonify({
#             "prediction_report": result.get("prediction_report", "No prediction report generated."),
#             "cyber_report": result.get("cyber_report", "No cybersecurity report generated.")
#         })

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(debug=True)