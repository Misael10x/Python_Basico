# Eliminar un archivo

import os
import shutil
 
path = 'folder'
 
try:
 
     #os.remove(path)
     #os.rmdir(path)
     shutil.rmtree(path)
except FileNotFoundError:
    print("Este archivo no existe")
except IsADirectoryError:
    print("Sorry no tienes permisos para eliminar la carpeta")
except OSError:
    print("No puedes eliminar eso usado esa funcion")
else:
    print("La carpeta fue eliminada")
