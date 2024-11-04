# Deteccion de archivos

import os

path = '/home/misael/Escritorio/hola'

if os.path.exists(path):
    print("Esa ubicacion existe")
    if os.path.isdir(path): # es un directorio
   # if os.path.isfile(path):  es un archivo
        print("Es un directorio")
else:
    print("Esa ubicacion no existe")