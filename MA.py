# Movimientos de archivo

import os

origen  = 'prueba.txt'
destino = '/home/misael/Escritorio/prueba.txt'


try:
    if os.path.exists(destino):
         print('Ya hay un archivoes este destino')
    else: 
         os.replace(origen, destino)
         print(origen + 'Fue movido')
except FileNotFoundError:
    print(origen + ' No fue encontrado')