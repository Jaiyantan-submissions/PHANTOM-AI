from flask import Flask, jsonify
from main import run_backend  # Import the backend logic from main.py

app = Flask(__name__)

@app.route('/')
def home():
    return "Cyber Threat Prediction and Deception System"

@app.route('/api/run_backend', methods=['GET'])
def run_backend_route():
    """Endpoint to trigger the backend processing."""
    result = run_backend()  # Calls the main processing function from main.py
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
