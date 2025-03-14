import numpy as np
from scipy.linalg import expm

def calcular_exponencial_matriz():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    
    A = np.zeros((n, n), dtype=complex)

    print("\nIntroduce los elementos de la matriz:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    exp_A = expm(A)
    
    print("\nExponencial de la matriz A:")
    for fila in exp_A:
        print(fila)

if __name__ == "__main__":
    calcular_exponencial_matriz()
