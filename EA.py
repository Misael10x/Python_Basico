# Escribir un archivo

texto = "\nWOW"

with open('test.txt', 'a')as file:    # a es para agregar y w es para escribir
    file.write(texto)