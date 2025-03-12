import numpy as np

def crear_matriz_compleja(filas, columnas):
    return np.random.rand(filas, columnas) + 1j * np.random.rand(filas, columnas)

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def operaciones_matriz(matriz):
    print("\nMatriz original:")
    imprimir_matriz(matriz)
    
    if matriz.shape[0] == matriz.shape[1]:
        det = np.linalg.det(matriz)
        print(f"\nDeterminante de la matriz: {det}")
