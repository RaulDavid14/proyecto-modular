from django.conf import settings
import requests

class Client():
    
    def __init__(self):
        self.url = settings.APIS['cfca_api_url']
        self.timeout = settings.APIS['timeout']
    
    def get_url(self, url):
        return f'{self.url}{url}'
    
    def get(self, endpoint, params=None):
        response = requests.get(f'{self.url}{endpoint}', params=params, timeout=self.timeout)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return None

    def save_respuesta(self, id_usuario, id_cuestionario, abreviacion, respuestas):
        data = {
            'id_usuario': id_usuario,
            'id_cuestionario': id_cuestionario,
            'abreviacion' : abreviacion,
            'respuestas': respuestas
        }
        requests.post(url = self.get_url('/respuestas/crear/'), json = data)
    
    
    def delete_respuesta(self, id_usuario, id_cuestionario, abreviacion):
        requests.delete(self.get_url(f'/respuestas/delete/{id_usuario}/{id_cuestionario}/{abreviacion}'))
    
    
    def create_progres(self, id_usuario):
        body = {
            'id_usuario' : id_usuario
        }
        
        requests.post(url=self.get_url('/respuestas/crear/progreso/'), json=body)