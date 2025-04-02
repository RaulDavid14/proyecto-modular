# PROYECTO


##  Bajar cambios del proyecto
    !!! IMPORTANTE 
    1    cuando se mencione que haya cambios en el repositorio de debe aplicar siempre el comando git pull, este comando se puede usar cuantas veces sea necesario y su funcion es validar si en el repositorio hay cambios, si los hay, se los llevara al proyecto en local. Es importante usar este comando antes de realizar algun cambio porque si se trabaja con la rama en la version que tienes en local al momento de subir tus cambios trabajados puedes borrar otros cambios realizados. 


    2   Ya que tienes el proyecto actualizado ejecuta el comando python manage.py runserver y en caso de existir algun error revisa lo siguiente:

        Revisa desde el git o sourcetree si existen cambios en archivos donde hayas trabajado, en caso de que si se va a hacer un conflicto, que es basicamente git diciendo que hay cambios diferentes y te da a elegir con cuales cambios te quedas. Otra cosa, si se hicieron cambios en los modelos, lo mas probable es que debas borrar el archivo sqli3 para aplicar los nuevos cambios.Estos cambios se aplican borrando la base de datos, luego ejecutar el comando python manage.py migrate y al final usar el comando loaddata utilizando los archivos json. 

        como se elimino la base de datos es necesario crear un nuevo usuario, para fines practicos ejecuta el comando python manage.py createsuperuser y sigue las indicaciones, ques estas son los datos para crear el usuario, una vez creados puedes interactuar con todo el sistema incluido el apartado 127.0.0.1:8000/admin

    3   Ejecuta nuevamente el comando python manage.py runserver para ver si no existen errores, en caso de que el arranque o durante la ejecucion del proyecto hay algun error, favor de notificarle al Raul mostrando lo que aparece en pantalla o en la terminal.

    4   En el caso de que al hacer todo lo anterior persiste el problema revisa el archivo manage.py en la linea 9 que tenga lo esto  "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.setting.local')" si tiene por ejemplo, local o produccion lo mas probable es que se me haya olvidado cambiarlo porque uso prueba, que es una conexion local de bases de datos parecida a la de produccion, de preferencia usa local que es el sqlite


    ## NOTA IMPORTANTE
    Si quieres usar una base de datos para ver mejor los datos puedes poner en la linea 9 en lugar de local prueba, que lo que hace es usar el archivo que se encuentra en proyecto/setting/prueba.py y cambiar las credenciales a las de tu base de datos, si es el caso que moviste esas credenciales, porfa no subas cambios de los siguientes archivos: manage.py y prueba.py para evitar conflictos con configuraciones de cada persona, no pasa nada si en git se dejan como modificados, de hecho 

    en git al momento de usar el comando git add . lo que pasa es que los archivos pasan a un status que se conoce como staged, que es prepararlos para subirlos al repositorio antes de hacerles commit, puede ser usar el git add . pero luedo debes usar este comando git restore --staged archivo1 archivo2 archivo3
    que sirve para indicarle a git la lista de archivos que quieres quitar, 

    o usar este comando git restore --staged . que quita todo de preparacion

## Cargar registros en la base 

Si quieres utilizar los registros de la base de datos sigue estos pasos

1. primero ejecuta el comando python manage.py makemigrations para asegurarte de aplicar tus cambios en el modelo.
    si el comando menciona que no hay cambios para aplicar puedes seguir

2. aplica el comando python manage.py migrate para crear las bases de datos en tu entorno local

3. Ya que termine de aplicar los esquemas el siguiente paso es cargar los datos a la base de datos

4. Con el comando python manage.py loaddata nombre?archivo.json insertas los registros en las tablas del
    proyecto, en el proyecto se encuentran tres archivos .json que contienen registros de prueba del proyecto.

5. Ya con los registros cargaso puedes ejecutar el proyecto con el comando python manage.py runserver

## APLICAR RESPALDOS
    cada que haya cambios en los modelos se hara un respaldo con la data actualizada.

    SI SE HICIERON CAMBIOS EN MODELOS PARA EVITAR QUE TODO TRUEN HAZ LO SIGUIENTE

    1. aplica el comando python manage.py aplication zero (esto revierte los cambios y borra las tablas)

    aplica el comando migrate con los cambios realiados

    aplica el loaddata para obtener los nuevos datos.


    
## Notas

-   El caso de hacer un nuevo modelo y que necesite datos es necesario crear un nuevo archivo json para 
que todos los integrantes puedan tener tus cambios

usa el comando python manage.py dumpdata nombre_de_la_aplicacion > respaldo.json para crear los archivos

-   Si vas hacer cambios sobre archivos que se encuentran en la carpeta static aplica el comando python manage.py collectstatic, este comando hace una copia con los archivos que se ejecutan en produccion.


## Nota Reestablecer pass
pip install mailjet-rest para el correo