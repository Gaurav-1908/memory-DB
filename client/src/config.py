import json
import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')

def config():
    try:
        with open(CONFIG_PATH) as f:
            config = json.load(f)
            return (config.get("server_url", "http://127.0.0.1:5000"), config.get("timeout", 5), config.get("password",""))
    except Exception as e:
        print(f"⚠️ Failed to load config: {e}")
        return "http://127.0.0.1:5000", 5, ""
