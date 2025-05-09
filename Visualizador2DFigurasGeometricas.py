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

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 3)
    ax.set_aspect('equal')
    plt.grid(True)
    plt.title("Figuras Geométricas 2D")
    plt.show()

if __name__ == "__main__":
    dibujar_figuras()
