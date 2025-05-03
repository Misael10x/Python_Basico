import numpy as np
A = np.array([[2, 3],
              [1, -1]])
B = np.array([8, 2])
X = np.linalg.solve(A, B)
