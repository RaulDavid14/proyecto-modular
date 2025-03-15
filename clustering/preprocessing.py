import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def preprocesar_datos(datos):
    if not datos:
        print("❌ No hay datos para preprocesar")
        return np.array([])

    # Encuentra la longitud de la lista más larga
    max_length = max(len(item) for item in datos)

    # Rellenar las listas más cortas con ceros (o cualquier otro valor que tenga sentido)
    for i in range(len(datos)):
        if len(datos[i]) < max_length:
            datos[i].extend([0] * (max_length - len(datos[i])))  # Rellenar con ceros
        elif len(datos[i]) > max_length:
            datos[i] = datos[i][:max_length]  # Recortar si la lista es más larga

    datos_np = np.array(datos)
    print("📊 Datos después de hacerlos homogéneos:", datos_np)

    print("📊 Datos antes de escalar:", datos_np)

    # Elegir el tipo de escalado dependiendo de la cantidad de datos
    if datos_np.shape[0] > 1:
        scaler = StandardScaler()
    else:
        scaler = MinMaxScaler()

    # Escalar los datos
    datos_escalados = scaler.fit_transform(datos_np)
    print("📊 Datos escalados:", datos_escalados)

    return datos_escalados

def limpiar_datos(datos):
    if not datos:
        print("No hay datos para limpiar")
        return []

    # Convertir a NumPy array para facilitar el manejo
    datos_np = np.array(datos, dtype=np.float64)

    # Eliminar filas con valores NaN o infinitos
    datos_np = datos_np[~np.isnan(datos_np).any(axis=1)]
    datos_np = datos_np[~np.isinf(datos_np).any(axis=1)]



    print("Datos después de la limpieza:", datos_np)

    return datos_np.tolist()  # Convertir de nuevo a lista para compatibilidad
