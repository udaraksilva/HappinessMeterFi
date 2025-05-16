from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='static')
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('employees.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/thankyou')
def thankyou():
    return send_from_directory('static', 'thankyou.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    employee_id = data.get('employee_id')
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM employees WHERE employee_id = ?", (employee_id,)).fetchone()
    conn.close()
    if user:
        return jsonify(success=True, name=user['first_name'])
    return jsonify(success=False, message="Invalid ID")

@app.route('/api/vote', methods=['POST'])
def vote():
    data = request.json
    # Placeholder logic
    return jsonify(success=True)

@app.route('/api/meter', methods=['GET'])
def meter():
    return jsonify(success=True, happy=80, sad=20)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
