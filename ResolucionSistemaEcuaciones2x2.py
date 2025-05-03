import numpy as np
A = np.array([[2, 3],
              [1, -1]])
B = np.array([8, 2])
X = np.linalg.solve(A, B)
print("Solución del sistema:")
print("x =", round(X[0], 2))
print("y =", round(X[1], 2))
verif = np.dot(A, X)
print("Verificación Ax =", verif)
