from flask import Flask, request, jsonify
from threading import Lock
import json

with open('config.json') as f:
    config = json.load(f)

ALLOWED_IPS = config.get("allowed_ips", ['localhost'])
PORT = config.get("port", 5000)

app = Flask(__name__)

class GDB:
    def __init__(self):
        self.store = {}
        self.lock = Lock()

    def put(self, data):
        with self.lock:
            self.store.update(data)

    def get(self, key):
        with self.lock:
            return self.store.get(key)

    def delete(self, key):
        with self.lock:
            if key in self.store:
                del self.store[key]
                return True
            return False

    def reset(self):
        with self.lock:
            self.store.clear()

    def exists(self, key):
        with self.lock:
            return key in self.store

    def get_all(self):
        with self.lock:
            return dict(self.store)

store = GDB()

@app.before_request
def limit_remote_addr():
    client_ip = request.remote_addr
    if client_ip not in ALLOWED_IPS:
        return jsonify({"error": "Forbidden", "message": f"Access denied for IP {client_ip}"}), 403

@app.route('/put', methods=['PUT'])
def put():
    data = request.get_json()
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input. JSON dictionary expected."}), 400
    store.put(data)
    return jsonify({"message": "Data inserted", "data": data}), 201

@app.route('/get/<key>', methods=['GET'])
def get(key):
    value = store.get(key)
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({key: value}), 200

@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):
    success = store.delete(key)
    if not success:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({"message": "Key deleted"}), 200

@app.route('/reset', methods=['POST'])  # or methods=['DELETE']
def reset():
    store.reset()
    return jsonify({"message": "Store reset"}), 200

@app.route('/exists/<key>', methods=['GET'])
def exists(key):
    if store.exists(key):
        return jsonify({"exists": True}), 200
    return jsonify({"exists": False}), 200

@app.route('/all', methods=['GET'])
def get_all():
    return jsonify(store.get_all()), 200

if __name__ == '__main__':
    app.run(debug=True,port=PORT)
