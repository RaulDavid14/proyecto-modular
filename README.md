# PROYECTO

## Cargar registros en la base 

Si quieres utilizar los registros de la base de datos sigue estos pasos

1. primero ejecuta el comando python manage.py makemigrations para asegurarte de aplicar tus cambios en el modelo.
    si el comando menciona que no hay cambios para aplicar puedes seguir

2. aplica el comando python manage.py migrate para crear las bases de datos en tu entorno local

3. Ya que termine de aplicar los esquemas el siguiente paso es cargar los datos a la base de datos

4. Con el comando python manage.py loaddata nombre?archivo.json insertas los registros en las tablas del
    proyecto, en el proyecto se encuentran tres archivos .json que contienen registros de prueba del proyecto.

5. Ya con los registros cargaso puedes ejecutar el proyecto con el comando python manage.py runserver




## Nota

El caso de hacer un nuevo modelo y que necesite datos es necesario crear un nuevo archivo json para 
que todos los integrantes puedan tener tus cambios

usa el comando python manage.py dumpdata nombre_de_la_aplicacion > respaldo.json para crear los archivos


## Nota Reestablecer pass
pip install mailjet-rest para el correo