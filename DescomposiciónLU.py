import numpy as np
from scipy.linalg import lu

def descomposicion_lu():
    n = int(input("Introduce el tamaño de la matriz cuadrada: "))
    A = np.random.randint(1, 10, (n, n))
    
    P, L, U = lu(A)

    print("\nMatriz A:\n", A)
    print("\nMatriz L:\n", L)
    print("\nMatriz U:\n", U)

if __name__ == "__main__":
    descomposicion_lu()
