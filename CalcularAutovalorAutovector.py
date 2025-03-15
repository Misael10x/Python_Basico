import numpy as np

def calcular_autovalores_autovectores():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    
    A = np.zeros((n, n), dtype=complex)
