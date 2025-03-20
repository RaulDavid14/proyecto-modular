import numpy as np
from sklearn.cluster import KMeans
from .data_extraction import obtener_datos_usuarios
from .preprocessing import preprocesar_datos, limpiar_datos
from catalogos.models import DatosGenerales

def aplicar_clustering():
    try:
        # Obtener los datos de usuarios
        datos = obtener_datos_usuarios()
        print("Datos obtenidos:", datos)

        # Preprocesar los datos
        datos_procesados = preprocesar_datos(datos)
        print("Datos procesados:", datos_procesados)
        
        
        # Limpiar los datos
        datos_limpios = limpiar_datos(datos)
        print("Datos limpios:", datos_limpios)

        # Verificar si los datos procesados están vacíos
        if datos_procesados.size == 0:
            print("No hay datos suficientes para clustering")
            return {"error": "No hay suficientes datos para clustering"}

        # Crear el modelo de clustering (KMeans)
        modelo = KMeans(n_clusters=4, random_state=42)
        modelo.fit(datos_procesados)

        # Obtener las etiquetas de los clusters
        etiquetas = modelo.labels_.tolist()
        print("Etiquetas de los clusters:", etiquetas)

        # Definir los niveles de consumo
        niveles_consumo = {0: "Bajo", 1: "Moderado", 2: "Normal", 3: "Excesivo"}

        # Obtener los usuarios de la base de datos
        usuarios = DatosGenerales.objects.all()
        print("Usuarios obtenidos:", list(usuarios))

        # Guardar los resultados de clustering
        resultados = []
        for i, usuario in enumerate(usuarios):
            nivel_consumo = niveles_consumo.get(etiquetas[i], "Desconocido")

            resultados.append({
                "user_id": usuario.id,
                "sexo_id": usuario.sexo.id if usuario.sexo else "Desconocido",
                "poblacion_id": usuario.poblacion.id if usuario.poblacion else "Desconocido",
                "nivel_educativo_id": usuario.nivel_educativo.id if usuario.nivel_educativo else "Desconocido",
                "cluster": nivel_consumo
            })

        print("Resultados de clustering:", resultados)
        return {"clustering": resultados}
    
    except Exception as e:
        print(" Error en aplicar_clustering:", e)
        return {"error": str(e)}

def guardar_resultados():
    return aplicar_clustering()

