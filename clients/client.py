from django.conf import settings
import requests

class Client():
    
    def __init__(self):
        self.url = settings.APIS['cfca_api_url']
        self.timeout = settings.APIS['timeout']
    
    def get(self, endpoint, params=None):
        response = requests.get(f'{self.url}{endpoint}', params=params, timeout=self.timeout)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None
    
    def save_respuesta(self):
        url = f'{self.url}/respuestas/create/'
        
        data = {
            
        }
        requests.post(url=url, data = data)
    
    def create_progres(self, id_usuario):
        url = f'{self.url}/respuestas/crear/progreso/'
        
        body = {
            'id_usuario' : id_usuario
        }
        
        requests.post(url=url, json=body)