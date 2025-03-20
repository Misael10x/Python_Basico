import numpy as np

def resolver_sistema_complejo():
    n = int(input("Introduce el número de ecuaciones y variables: "))
    
    A = np.zeros((n, n), dtype=complex)
    B = np.zeros(n, dtype=complex)

    print("\nIntroduce los coeficientes del sistema (matriz A):")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    print("\nIntroduce los términos independientes (vector B):")
    for i in range(n):
        real = float(input(f"Parte real de B[{i+1}]: "))
        imag = float(input(f"Parte imaginaria de B[{i+1}]: "))
        B[i] = complex(real, imag)
