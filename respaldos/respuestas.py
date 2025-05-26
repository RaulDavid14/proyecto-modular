from usuario.models import UserModel
from faker import Faker
import random
from usuario.models import UserModel
from catalogos.models import CatPoblacion, CatSexo, CatNivelEducativo
from catalogos.models import DatosGenerales

"""
fake = Faker()
NUM_USUARIOS = 50

for i in range(NUM_USUARIOS):
    nombre_completo = fake.name()
    email = fake.email()
    password = fake.password()
    
    user = UserModel.objects.create_user(
        email=email,
        password=password,
        nombre_completo=nombre_completo,
        second_name=fake.first_name(),
        third_name=fake.first_name(),
        last_name_maternal=fake.last_name(),
        birth_date=fake.date_of_birth(),
    )
    
    print(f"Usuario {i+1}: {email} creado.")

print("Usuarios de prueba creados.")
"""



poblaciones = list(CatPoblacion.objects.filter(id__in=[1, 2]))
sexos = list(CatSexo.objects.filter(id__in=[1, 2]))
niveles_educativos = list(CatNivelEducativo.objects.filter(id__range=(1, 6)))

usuarios = UserModel.objects.all()

for usuario in usuarios:
    if not DatosGenerales.objects.filter(user=usuario).exists():
        DatosGenerales.objects.create(
            user=usuario,
            poblacion=random.choice(poblaciones) if poblaciones else None,
            sexo=random.choice(sexos) if sexos else None,
            nivel_educativo=random.choice(niveles_educativos) if niveles_educativos else None
        )
        print(f"Registro de DatosGenerales creado para el usuario: {usuario.email}")

print("DatosGenerales creados aleatoriamente para todos los usuarios.")


import random
from usuario.models import UserModel
from cuestionario.models import PreguntaModel, RespuestaModel

usuarios = UserModel.objects.all()

preguntas = PreguntaModel.objects.all()

for usuario in usuarios:
    for pregunta in preguntas:
        respuesta_aleatoria = random.randint(1, 9)
        
        RespuestaModel.objects.create(
            id_usuario=usuario.id,
            id_cuestionario=pregunta.tipo_cuestionario, 
            no_pregunta=pregunta.id, 
            id_respuesta=respuesta_aleatoria
        )

print("Respuestas aleatorias generadas para todos los usuarios.")
