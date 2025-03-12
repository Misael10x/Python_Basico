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
    
    try:
        inversa = np.linalg.inv(matriz)
        print("\nInversa de la matriz:")
        imprimir_matriz(inversa)
    except np.linalg.LinAlgError:
        print("\nLa matriz no es invertible.")
    
    transpuesta = np.transpose(matriz)
    print("\nTranspuesta de la matriz:")
    imprimir_matriz(transpuesta)

def main():
    filas = int(input("Introduce el número de filas: "))
    columnas = int(input("Introduce el número de columnas: "))
    
    matriz_compleja = crear_matriz_compleja(filas, columnas)
    operaciones_matriz(matriz_compleja)

if __name__ == "__main__":
    main()
