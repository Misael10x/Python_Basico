import matplotlib
matplotlib.use('Agg')  # Usa el backend sin GUI
import numpy as np
import matplotlib.pyplot as plt

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(6,6))

# Dibujar el círculo
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2)
ax.add_patch(circle)

# Dibujar los ejes x e y
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)

# Marcar los puntos importantes
points = {"(1,0)": (1, 0), "(-1,0)": (-1, 0), "(0,1)": (0, 1), "(0,-1)": (0, -1)}
for label, (x, y) in points.items():
    ax.plot(x, y, 'ro')  # Puntos en rojo
    ax.text(x, y, f' {label}', fontsize=12, verticalalignment='bottom' if y >= 0 else 'top')
