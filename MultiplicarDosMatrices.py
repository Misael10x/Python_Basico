import numpy as np

def multiplicar_matrices_complejas():
    n = int(input("Introduce el tamaño de la matriz (n x n): "))
    
    A = np.zeros((n, n), dtype=complex)
    B = np.zeros((n, n), dtype=complex)

    print("\nIntroduce los elementos de la primera matriz A:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    print("\nIntroduce los elementos de la segunda matriz B:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de B[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de B[{i+1}][{j+1}]: "))
            B[i, j] = complex(real, imag)

    C = np.dot(A, B)

    print("\nResultado de la multiplicación de A por B:")
    for fila in C:
        print(fila)

if __name__ == "__main__":
    multiplicar_matrices_complejas()
