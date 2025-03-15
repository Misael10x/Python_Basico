import numpy as np

def calcular_autovalores_autovectores():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    
    A = np.zeros((n, n), dtype=complex)

    print("\nIntroduce los elementos de la matriz:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    autovalores, autovectores = np.linalg.eig(A)

    print("\nAutovalores de la matriz A:")
    for val in autovalores:
        print(val)
