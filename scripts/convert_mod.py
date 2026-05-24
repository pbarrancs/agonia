import os
import subprocess


def convertir_mod_a_mp4(carpeta_entrada, carpeta_salida):
    # Crear la carpeta de salida si no existe
    os.makedirs(carpeta_salida, exist_ok=True)

    # Recorre todos los archivos de la carpeta
    for archivo in os.listdir(carpeta_entrada):
        if archivo.lower().endswith('.mod'):
            ruta_entrada = os.path.join(carpeta_entrada, archivo)

            # Renombrar archivo de salida con extensión .mp4
            nombre_base = os.path.splitext(archivo)[0]
            ruta_salida = os.path.join(carpeta_salida, nombre_base + '.mp4')

            # Comando de conversión con ffmpeg
            comando = [
                'ffmpeg',
                '-i', ruta_entrada,
                # Codec de video (puedes cambiar por copy si solo quieres remux)
                '-c:v', 'libx264',
                '-c:a', 'aac',       # Codec de audio
                '-strict', 'experimental',
                ruta_salida
            ]

            print(f"Convirtiendo {archivo} a MP4...")
            subprocess.run(comando, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    print("Conversión completada.")


# Ejemplo de uso
carpeta_mods = 'PRG003'
carpeta_mp4 = 'PRG003_mp4'
convertir_mod_a_mp4(carpeta_mods, carpeta_mp4)
