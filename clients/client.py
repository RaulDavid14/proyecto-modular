from django.conf import settings
import requests

class Client():
    
    def __init__(self):
        self.url = settings.APIS['url']
        self.timeout = settings.APIS['timeout']
    
    def get(self, endpoint, params=None):
        response = requests.get(f'{self.url}{endpoint}', params=params, timeout=self.timeout)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
        