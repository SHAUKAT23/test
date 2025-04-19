# filepath: backend/app.py
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import os
from datetime import datetime, timedelta
import pytz  # For timezone handling

app = Flask(__name__, template_folder='templates')
CORS(app)  # Enable CORS for potential future frontend

def get_indian_time():
    tz_ist = pytz.timezone('Asia/Kolkata')
    now_utc = datetime.utcnow()
    now_ist = now_utc.astimezone(tz_ist)
    return now_ist

@app.route('/')
def index():
    tournament_name = "SPECTRUM TOURNAMENT"
    match_type = "KHO-KHO MATCHES"
    venue = "TMC Ground"
    matches = [
        {"type": "bronze", "teams": "BRONZE MATCH: BE vs UG",
         "date": get_indian_time().strftime('%A, %dth %B %Y'), "time": "7:30 PM"},
        {"type": "final", "teams": "FINAL MATCH: Civil vs Staff",
         "date": (get_indian_time() + timedelta(days=1)).strftime('%A, %dth %B %Y'), "time": "9:30 PM"}
    ]
    pools_men = {}  # No longer relevant for just finals/bronze
    schedule_round1 = [] # No longer relevant

    return render_template('index.html',
                           tournament_name=tournament_name,
                           match_type=match_type,
                           venue=venue,
                           matches=matches,
                           pools_men=pools_men,
                           schedule_round1=schedule_round1)

@app.route('/api/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        data = request.json
        return jsonify({"message": "Comment received!", "data": data}), 201
    return jsonify({"comments": ["Great match!", "Go team!"]})

@app.route('/debug/files', methods=['GET'])
def list_files():
    return jsonify(os.listdir('.'))

if __name__ == '__main__':
    app.run(debug=True)