import os
import subprocess
from pathlib import Path


def convertir_mts_a_mp4(carpeta_entrada, carpeta_salida):
    # Crear la carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)

    # Recorre todos los archivos en la carpeta de entrada
    for archivo in os.listdir(carpeta_entrada):
        if archivo.lower().endswith('.mts'):
            ruta_entrada = os.path.join(carpeta_entrada, archivo)
            nombre_base = os.path.splitext(archivo)[0]
            ruta_salida = os.path.join(carpeta_salida, nombre_base + '.mp4')

            # Comando ffmpeg: copiar video sin recomprimir si se desea (más rápido) o recodificar
            comando = [
                'ffmpeg',
                '-i', ruta_entrada,
                '-c:v', 'libx264',   # codec de video H.264
                '-preset', 'fast',   # velocidad de compresión
                '-crf', '22',        # calidad (menor número = mayor calidad)
                '-c:a', 'aac',       # codec de audio AAC
                '-b:a', '192k',      # bitrate de audio
                ruta_salida
            ]

            print(f"Convirtiendo {archivo} a MP4...")
            subprocess.run(comando, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    print("Todas las conversiones han terminado.")


dir_path = Path('Rogers_Frens')

# Verifica si la carpeta existe
if not dir_path.exists():
    print(f"La carpeta {dir_path} no existe.")

# Ejemplo de uso
carpeta_mts = dir_path / 'mts'
carpeta_mp4 = dir_path / 'mp4'
convertir_mts_a_mp4(carpeta_mts, carpeta_mp4)
