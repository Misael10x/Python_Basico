import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

G = 6.67430e-11  
dt = 24 * 3600  
num_dias = 365  
num_pasos = num_dias  

class Planeta:
    def __init__(self, nombre, masa, posicion, velocidad):
        self.nombre = nombre
        self.masa = masa
        self.posicion = np.array(posicion, dtype=np.float64)
        self.velocidad = np.array(velocidad, dtype=np.float64)
        self.trayectoria = []

    def actualizar_trayectoria(self):
        self.trayectoria.append(self.posicion.copy())

def calcular_fuerza(gravedad, planeta1, planeta2):
    r = planeta2.posicion - planeta1.posicion
    distancia = np.linalg.norm(r)
    if distancia == 0:
        return np.array([0, 0, 0])
    fuerza = gravedad * planeta1.masa * planeta2.masa / distancia**3 * r
    return fuerza

def simular_sistema():
    sol = Planeta("Sol", 1.989e30, [0, 0, 0], [0, 0, 0])
    tierra = Planeta("Tierra", 5.972e24, [1.496e11, 0, 0], [0, 29780, 0])

    planetas = [sol, tierra]

    for _ in range(num_pasos):
        fuerzas = {p: np.array([0, 0, 0], dtype=np.float64) for p in planetas}

        for i in range(len(planetas)):
            for j in range(i + 1, len(planetas)):
                f = calcular_fuerza(G, planetas[i], planetas[j])
                fuerzas[planetas[i]] += f
                fuerzas[planetas[j]] -= f

        for planeta in planetas:
            planeta.velocidad += (fuerzas[planeta] / planeta.masa) * dt
            planeta.posicion += planeta.velocidad * dt
            planeta.actualizar_trayectoria()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for planeta in planetas:
        trayectoria = np.array(planeta.trayectoria)
        ax.plot(trayectoria[:, 0], trayectoria[:, 1], trayectoria[:, 2], label=planeta.nombre)

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.set_title("Simulación del Sistema Solar")
    ax.legend()
    plt.show()

if __name__ == "__main__":
    simular_sistema()
