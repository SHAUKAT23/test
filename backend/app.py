# filepath: backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for React

# Example route
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