import numpy as np

def potencia_matriz_compleja():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    p = int(input("Introduce la potencia a la que deseas elevar la matriz: "))

    A = np.zeros((n, n), dtype=complex)

    print("\nIntroduce los elementos de la matriz:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    resultado = np.linalg.matrix_power(A, p)

    print(f"\nMatriz A elevada a la potencia {p}:")
    for fila in resultado:
        print(fila)
