import requests

class APIClient:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def put(self, key, value, password):
        return requests.put(f'{self.base_url}/put', headers={'X-Password': password}, json={key: value}, timeout=self.timeout)

    def get(self, key, password):
        return requests.get(f'{self.base_url}/get/{key}', headers={'X-Password': password}, timeout=self.timeout)

    def delete(self, key, password):
        return requests.delete(f'{self.base_url}/delete/{key}', headers={'X-Password': password}, timeout=self.timeout)

    def exists(self, key, password):
        return requests.get(f'{self.base_url}/exists/{key}', headers={'X-Password': password}, timeout=self.timeout)

    def reset(self, password):
        return requests.post(f'{self.base_url}/reset',  headers={'X-Password': password}, timeout=self.timeout)

    def get_all(self, password):
        return requests.get(f'{self.base_url}/all' ,headers={'X-Password': password}, timeout=self.timeout)
    
    def backup(self, password):
        return requests.get(f'{self.base_url}/backup' ,headers={'X-Password': password}, timeout=self.timeout)
