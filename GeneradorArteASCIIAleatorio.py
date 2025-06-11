import random

caracteres = ['#', '*', '+', '@', '%', '&', '$']
filas = 20
columnas = 50

for _ in range(filas):
    linea = ''.join(random.choice(caracteres) for _ in range(columnas))
