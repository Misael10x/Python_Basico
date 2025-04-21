import matplotlib.pyplot as plt
import numpy as np

def dibujar_figuras():
    fig, ax = plt.subplots()

    # Círculo
    circulo = plt.Circle((1, 1), 0.5, color='blue', fill=False)
    ax.add_patch(circulo)
