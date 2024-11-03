# Copiando archivos

# copyfile()   copea un contenido de un archivo a otro
# copy()   hace lo mismo que copyfile ademas de los permisos y el destino puede ser un directorio
# copy2()   hace lo que hace copy() ademas de los metodos y las fechas de creacion y modificacion

import shutil

shutil.copyfile('test.txt', 'copy.txt')

