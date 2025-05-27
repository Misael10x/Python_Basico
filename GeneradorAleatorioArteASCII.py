import random

ancho = int(input("Ancho del arte: "))
alto = int(input("Alto del arte: "))

simbolos = ['#', '*', '+', '=', '-', '~', '^', '@', '%', '&']

for _ in range(alto):
    linea = ''.join(random.choice(simbolos) for _ in range(ancho))
    print(linea)
