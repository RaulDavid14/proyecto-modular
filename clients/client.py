from django.conf import settings
import requests

class Client():
    
    def __init__(self):
        self.url = settings.APIS['cfca_api_url']
        self.timeout = settings.APIS['timeout']
    
    def get_url(self, url):
        return f'{self.url}{url}'

    def get(self, endpoint, params=None):
        try:
            response = requests.get(
                f'{self.url}{endpoint}', 
                params=params, 
                timeout=self.timeout
            )
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                return None
            else:
                print(f'GET {endpoint} → Código inesperado: {response.status_code}')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Error en GET {endpoint}: {e}')
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
    
    def save_datos_generales(
        self, id_usuario, situacion_laboral, ingresos, sexo, poblacion, nivel_educativo 
    ):
        body = {
            "usuario" : id_usuario
            ,"situacion_laboral" : situacion_laboral
            ,"ingresos" : ingresos
            ,"sexo" : sexo
            ,"poblacion" : poblacion
            ,"nivel_educativo" : nivel_educativo
        }
        
        requests.post(self.get_url('/respuestas/guardar/datosgenerales'), json=body)
    
    def update_datos_generales(
        self, id_usuario, situacion_laboral, ingresos, sexo, poblacion, nivel_educativo
    ):

        body = {
            "usuario" : id_usuario
            ,"situacion_laboral" : situacion_laboral
            ,"ingresos" : ingresos
            ,"sexo" : sexo
            ,"poblacion" : poblacion
            ,"nivel_educativo" : nivel_educativo
        }
        
        requests.put(self.get_url(f'/respuestas/datosgenerales/{id_usuario}'), json=body)
        
    def create_progres(self, id_usuario):
        body = {
            'id_usuario': id_usuario
        }
        try:
            response = requests.post(
                url=self.get_url('/respuestas/crear/progreso/'),
                json=body,
                timeout=self.timeout
            )
            if response.status_code != 200:
                print(f'Error al crear progreso: código {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f'Error al crear progreso: {e}')
