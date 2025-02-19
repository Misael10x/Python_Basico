import tkinter as tk

# Configuración inicial
ANCHO = 800
ALTO = 600
NIVELES = 5  # Niveles de recursión para el fractal

# Función para dibujar el Triángulo de Sierpinski
def dibujar_sierpinski(x1, y1, x2, y2, x3, y3, nivel):
    if nivel == 0:
        # Dibujar el triángulo
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="blue", outline="black")
