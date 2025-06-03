import numpy as np
import matplotlib.pyplot as plt

n0 = 1000
p = 0.01
tiempo = 100
n = [n0]

for t in range(1, tiempo):
    desintegrados = np.random.binomial(n[-1], p)
    n.append(n[-1] - desintegrados)

plt.plot(n, color='orange')
plt.title("Simulación de Desintegración Radiactiva")
plt.xlabel("Tiempo")
plt.ylabel("Átomos restantes")
plt.grid(True)
plt.show()
