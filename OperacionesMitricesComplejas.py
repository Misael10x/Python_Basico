import numpy as np

def crear_matriz_compleja(filas, columnas):
    return np.random.rand(filas, columnas) + 1j * np.random.rand(filas, columnas)
