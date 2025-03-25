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
