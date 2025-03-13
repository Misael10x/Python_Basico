import numpy as np

def resolver_sistema_complejo():
    n = int(input("Introduce el número de ecuaciones (y variables): "))
    
    A = np.zeros((n, n), dtype=complex)
    B = np.zeros(n, dtype=complex)

    print("\nIntroduce los coeficientes de la matriz A:")
    for i in range(n):
        for j in range(n):
            real = float(input(f"Parte real de A[{i+1}][{j+1}]: "))
            imag = float(input(f"Parte imaginaria de A[{i+1}][{j+1}]: "))
            A[i, j] = complex(real, imag)

    print("\nIntroduce los valores del vector B:")
    for i in range(n):
        real = float(input(f"Parte real de B[{i+1}]: "))
        imag = float(input(f"Parte imaginaria de B[{i+1}]: "))
        B[i] = complex(real, imag)

    try:
        X = np.linalg.solve(A, B)
        print("\nSolución del sistema:")
        for i, x in enumerate(X):
            print(f"X[{i+1}] = {x}")
    except np.linalg.LinAlgError:
        print("\nEl sistema no tiene solución única.")

if __name__ == "__main__":
    resolver_sistema_complejo()
