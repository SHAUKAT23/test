# filepath: backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for React

# Example route
@app.route('/api/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        data = request.json
        return jsonify({"message": "Comment received!", "data": data}), 201
    return jsonify({"comments": ["Great match!", "Go team!"]})

if __name__ == '__main__':
    app.run(debug=True)