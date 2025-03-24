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

    t_max = 10  
    t_eval = np.linspace(0, t_max, 300)

    solucion = solve_ivp(pendulo, [0, t_max], [theta0, omega0], t_eval=t_eval, args=(g, l))

    plt.figure()
    plt.plot(t_eval, np.degrees(solucion.y[0]))
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Ángulo (°)")
    plt.title("Movimiento de un péndulo simple")
    plt.grid()
    plt.show()
