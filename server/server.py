from flask import Flask, request, jsonify
import json,os
from src.Store import Store

with open('config.json') as f:
    config = json.load(f)

ALLOWED_IPS = config.get("allowed_ips", ['localhost'])
PORT = config.get("port", 5000)
SECURITY = config.get("security","OFF")
PASSWORD = config.get("password","")

app = Flask(__name__)
store = Store()

@app.before_request
def limit_remote_addr():
    client_ip = request.remote_addr
    password = request.headers.get("X-Password")
    print(password)
    if client_ip not in ALLOWED_IPS:
        return jsonify({"error": "Forbidden", "message": f"Access denied for IP {client_ip}"}), 403
    if ( SECURITY == "ON" and password != PASSWORD):
        return jsonify({"error": "Forbidden", "message": f"Access denied due to wrong passowrd"}), 403



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


@app.route('/backup')
def backup():
    data = store.get_all()  # Get all key-value pairs
    backup_path = os.path.join(os.path.dirname(__file__), 'backup.json')

    try:
        with open(backup_path, 'w') as f:
            json.dump(data, f, indent=2)
        return jsonify({
            "message": "Backup created successfully.",
            "data": data
        }), 200
    except Exception as e:
        return jsonify({
            "error": "Backup failed",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True,port=PORT)
