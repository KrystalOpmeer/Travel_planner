from flask import Flask, request, jsonify
from App2 import generate_plan  # Import your travel plan algorithm

app = Flask(__name__)

# Manually Enable CORS
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"  # Allow requests from any domain
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route('/generate_plan', methods=['POST'])
def get_travel_plan():
    data = request.json  # Receive user input from frontend
    if not data:
        return jsonify({"error": "Invalid request. No data received."}), 400

    try:
        plan = generate_plan(
            start=data.get('start'),
            place_type=data.get('place_type'),
            max_travel_hours=data.get('max_travel_hours'),
            budget=data.get('budget'),
            num_days=data.get('num_days'),
            return_to_start=data.get('return_to_start', False)  # Default to False if not provided
        )
        return jsonify(plan)

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors gracefully

if __name__ == '__main__':
    app.run(debug=True)
