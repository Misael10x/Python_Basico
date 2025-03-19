import numpy as np

def diagonalizar_matriz_compleja():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    
    A = np.zeros((n, n), dtype=complex)

    print("\nIntroduce los elementos de la matriz:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    valores, vectores = np.linalg.eig(A)

    D = np.diag(valores)
    P = vectores
    P_inv = np.linalg.inv(P)
