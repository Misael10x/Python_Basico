import numpy as np
import matplotlib.pyplot as plt

n0 = 1000
p = 0.01
tiempo = 100
n = [n0]

for t in range(1, tiempo):
    desintegrados = np.random.binomial(n[-1], p)
