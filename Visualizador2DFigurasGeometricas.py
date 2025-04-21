import matplotlib.pyplot as plt
import numpy as np

def dibujar_figuras():
    fig, ax = plt.subplots()

    # Círculo
    circulo = plt.Circle((1, 1), 0.5, color='blue', fill=False)
    ax.add_patch(circulo)

    # Cuadrado
    cuadrado = plt.Rectangle((2, 0.5), 1, 1, edgecolor='green', fill=False)
    ax.add_patch(cuadrado)

    # Triángulo
    triangulo = plt.Polygon([[4, 0.5], [4.5, 1.5], [5, 0.5]], closed=True, edgecolor='red', fill=False)
    ax.add_patch(triangulo)

    # Rectángulo
    rectangulo = plt.Rectangle((6, 0.5), 1.5, 1, edgecolor='purple', fill=False)
    ax.add_patch(rectangulo)
