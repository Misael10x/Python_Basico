import numpy as np

def svd_matriz_compleja():
    n = int(input("Introduce el tamaño de la matriz (n x n): "))
    
    A = np.zeros((n, n), dtype=complex)

    print("\nIntroduce los elementos de la matriz:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    U, S, Vh = np.linalg.svd(A)

    print("\nMatriz U (vectores singulares izquierdos):")
    for fila in U:
        print(fila)

    print("\nValores singulares:")
    print(S)

    print("\nMatriz Vh (vectores singulares derechos transpuestos):")
    for fila in Vh:
        print(fila)

if __name__ == "__main__":
    svd_matriz_compleja()
