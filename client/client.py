import requests
import json
import os

# Load configuration
CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
try:
    with open(CONFIG_PATH) as f:
        config = json.load(f)
        API_URL = config.get("server_url", "http://127.0.0.1:5000")
        TIMEOUT = config.get("timeout", 5)
except Exception as e:
    print(f"⚠️ Failed to load config: {e}")
    API_URL = "http://127.0.0.1:5000"
    TIMEOUT = 5

def put(key, value):
    try:
        response = requests.put(f'{API_URL}/put', json={key: value}, timeout=TIMEOUT)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def get(key):
    try:
        response = requests.get(f'{API_URL}/get/{key}', timeout=TIMEOUT)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def delete(key):
    try:
        response = requests.delete(f'{API_URL}/delete/{key}', timeout=TIMEOUT)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def exists(key):
    try:
        response = requests.get(f'{API_URL}/exists/{key}', timeout=TIMEOUT)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def reset():
    try:
        response = requests.post(f'{API_URL}/reset', timeout=TIMEOUT)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def get_all():
    try:
        response = requests.get(f'{API_URL}/all', timeout=TIMEOUT)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def show_help():
    print("""
Commands:
  put <key> <value>    - Insert or update key
  get <key>            - Retrieve value for key
  delete <key>         - Delete key
  exists <key>         - Check if key exists
  reset                - Clear the entire store
  all                  - Show all key-value pairs
  help                 - Show this help message
  exit                 - Exit CLI
""")

def cli():
    print("🔑 Welcome to GDB CLI!")
    print(f"📡 Connected to: {API_URL} (timeout: {TIMEOUT}s)")
    show_help()
    while True:
        try:
            user_input = input(">>> ").strip().split()
            if not user_input:
                continue

            command = user_input[0].lower()

            if command == 'put' and len(user_input) == 3:
                put(user_input[1], user_input[2])
            elif command == 'get' and len(user_input) == 2:
                get(user_input[1])
            elif command == 'delete' and len(user_input) == 2:
                delete(user_input[1])
            elif command == 'exists' and len(user_input) == 2:
                exists(user_input[1])
            elif command == 'reset':
                reset()
            elif command == 'all':
                get_all()
            elif command == 'help':
                show_help()
            elif command == 'exit':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid command. Type 'help' for instructions.")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == '__main__':
    cli()
