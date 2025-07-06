def handle_response(func, *args):
    try:
        response = func(*args)
        print(response.json())
    except Exception as e:
        print(f"❌ Request failed: {e}")

def put(client, key, value, password):
    handle_response(client.put, key, value, password)

def get(client, key, password):
    handle_response(client.get, key, password)

def delete(client, key, password):
    handle_response(client.delete, key, password)

def exists(client, key, password):
    handle_response(client.exists, key, password)

def reset(client, password):
    handle_response(client.reset, password)

def get_all(client, password):
    handle_response(client.get_all, password)

def backup(client,password):
    handle_response(client.backup, password)