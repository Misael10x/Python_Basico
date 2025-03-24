import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def pendulo(t, y, g, l):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]

def simular_pendulo():
    g = 9.81  
    l = float(input("Introduce la longitud del péndulo (m): "))
    theta0 = np.radians(float(input("Introduce el ángulo inicial (grados): ")))
    omega0 = 0
