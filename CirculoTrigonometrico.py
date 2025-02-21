import matplotlib
matplotlib.use('Agg')  # Usa el backend sin GUI
import numpy as np
import matplotlib.pyplot as plt

# Crear la figura y el eje
fig, ax = plt.subplots(figsize=(6,6))

# Dibujar el círculo
circle = plt.Circle((0, 0), 1, color='blue', fill=False, linewidth=2)
ax.add_patch(circle)
