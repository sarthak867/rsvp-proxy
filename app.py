from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwWM6_kaFaTTAqWga7n3K-kKQXrxwKiVm8VVfWX-4RI4q--OrXcxAGuGREU2Q_RZA8Uxw/exec"

@app.route('/rsvp-proxy', methods=['POST'])
def proxy_rsvp():
    try:
        data = request.get_json()
        response = requests.post(GOOGLE_SCRIPT_URL, json=data)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/')
def home():
    return "RSVP Proxy is running"

if __name__ == '__main__':
    app.run()
