import numpy as np

def potencia_matriz_compleja():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    p = int(input("Introduce la potencia a la que deseas elevar la matriz: "))

    A = np.zeros((n, n), dtype=complex)
