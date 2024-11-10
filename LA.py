# Leer un archivo
try:
    with open('hola.txt') as file:
        print(file.read())  # lee el archivo
except FileNotFoundError:
    print('El archivo no fue encontrado')
    
    
    
# print(file.closed)  # cierra el archivo