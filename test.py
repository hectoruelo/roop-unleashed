import os
import shutil
import time

# Directorio de origen
directorio_origen = '/ruta/del/directorio/origen'

# Directorio de destino
directorio_destino = '/ruta/del/directorio/destino'

# Palabra clave a buscar en el nombre del archivo
palabra_clave = 'temp'

while True:
    # Obtener la lista de archivos en el directorio de origen
    archivos = os.listdir(directorio_origen)

    for archivo in archivos:
        # Verificar si la palabra clave está presente en el nombre del archivo
        if palabra_clave not in archivo:
            # Construir las rutas completas
            ruta_origen = os.path.join(directorio_origen, archivo)
            ruta_destino = os.path.join(directorio_destino, archivo)

            try:
                # Mover el archivo al directorio de destino
                shutil.move(ruta_origen, ruta_destino)
                print(f'Archivo "{archivo}" movido a "{directorio_destino}".')
            except Exception as e:
                print(f'Error al mover el archivo "{archivo}". Error: {e}')

    # Esperar un intervalo antes de volver a revisar
    tiempo_espera = 300  # 5 minutos
    time.sleep(tiempo_espera)
