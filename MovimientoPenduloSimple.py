import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def pendulo(t, y, g, l):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - (g / l) * np.sin(theta)
    return [dtheta_dt, domega_dt]
  
