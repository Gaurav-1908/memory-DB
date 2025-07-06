from threading import Lock

class Store:
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