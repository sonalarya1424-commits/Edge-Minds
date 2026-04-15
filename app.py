from flask import Flask, request, jsonify, send_file
import random
import json
import google.generativeai as genai

app = Flask(__name__)

# ================== 🔑 PUT YOUR REAL GEMINI API KEY HERE ==================
# Get free key from: https://aistudio.google.com/app/apikey
genai.configure(api_key="your-api-key")   # ←←← CHANGE THIS

# Updated model (fixes the 404 "gemini-1.5-flash not found" error)
model = genai.GenerativeModel("gemini-2.5-flash")


# ===== AI + CYBERSECURITY LOGIC =====
def analyze_system(vibration, sound, temperature, rpm, network_delay):
    if vibration == 1 or sound > 600 or temperature > 50:
        prediction = "Anomaly Detected"
    else:
        prediction = "Normal"

    cyber_alerts = []
    if rpm < 300 and vibration == 1:
        cyber_alerts.append("Possible Sensor Spoofing (RPM mismatch)")
    if network_delay > 80:
        cyber_alerts.append("Possible MITM Attack (High Network Delay)")
    if temperature > 60 and sound < 200:
        cyber_alerts.append("Possible System Tampering")

    cyber_result = " | ".join(cyber_alerts) if cyber_alerts else "No cyber threat detected"

    return prediction, cyber_result


# ===== HOME ROUTE =====
@app.route('/')
def home():
    return send_file("frontend.html")


# ===== MANUAL PREDICTION =====
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        vibration = float(data["vibration"])
        temperature = float(data["temperature"])
        sound = float(data["sound"])
        rpm = float(data["rpm"])
        network_delay = float(data["network_delay"])

        prediction, cyber = analyze_system(vibration, sound, temperature, rpm, network_delay)

        return jsonify({
            "prediction": prediction,
            "cyber": cyber
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# ===== AUTO SIMULATION =====
@app.route('/simulate')
def simulate():
    data = {
        "vibration": random.choice([0, 1]),
        "temperature": random.randint(25, 70),
        "pressure": random.randint(1, 10),
        "voltage": random.randint(200, 250),
        "current": round(random.uniform(0.5, 5.0), 2),
        "rpm": random.randint(100, 2000),
        "network_delay": random.randint(1, 120),
        "device_id": random.randint(1, 5),
        "sound": random.randint(200, 800),
        "humidity": random.randint(30, 80)
    }

    prediction, cyber = analyze_system(
        data["vibration"], data["sound"], data["temperature"],
        data["rpm"], data["network_delay"]
    )

    data["prediction"] = prediction
    data["cyber"] = cyber
    return jsonify(data)


# ===== 🤖 FIXED AI FAILURE REPORT =====
@app.route('/generate_reports', methods=['POST'])
def generate_reports():
    try:
        data = request.get_json()
        prediction = data.get("prediction", "Normal")
        cyber = data.get("cyber", "No cyber threat detected")

        prompt = f"""
You are an expert industrial IoT security and predictive maintenance AI.

Machine Status:
- Prediction: {prediction}
- Cybersecurity Alerts: {cyber}

Return **ONLY** valid JSON. No explanations, no markdown, no extra text.

{{
  "prediction_report": "Technical explanation of why the machine is normal or in anomaly state (max 60 words)",
  "cyber_report": "Cybersecurity risk analysis and possible attack vectors (max 60 words)"
}}
"""

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.1,
                "max_output_tokens": 500,
                "response_mime_type": "application/json"   # Forces structured JSON output
            }
        )

        text = response.text.strip()

        # === Advanced Cleaning for Gemini output ===
        # Remove markdown code blocks
        if text.startswith("```"):
            text = text.split("```")[1].strip()
            if text.lower().startswith("json"):
                text = text[4:].strip()

        # Extract JSON if extra text exists
        start = text.find('{')
        end = text.rfind('}') + 1
        if start != -1 and end > start:
            text = text[start:end]

        # Parse JSON
        result = json.loads(text)

        return jsonify({
            "prediction_report": result.get("prediction_report", "Report generation failed"),
            "cyber_report": result.get("cyber_report", "Report generation failed")
        })

    except json.JSONDecodeError as je:
        # Show raw output for debugging
        return jsonify({
            "prediction_report": "JSON Parsing Failed",
            "cyber_report": f"AI returned invalid JSON. Raw: {text[:400]}..."
        }), 500

    except Exception as e:
        return jsonify({
            "prediction_report": "AI Report Error",
            "cyber_report": f"Error: {str(e)}"
        }), 500


# ===== RUN APP =====
if __name__ == '__main__':
    print("🚀 Starting Industrial IoT Monitor with Gemini 2.5 Flash...")
    app.run(debug=True)