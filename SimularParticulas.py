import tkinter as tk
import random

# Configuración inicial
ANCHO = 800
ALTO = 600
NUM_PARTICULAS = 50  # Número de partículas
COLORES = ["red", "green", "blue", "yellow", "cyan", "magenta", "orange"]

# Clase para representar una partícula
class Particula:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tamaño = random.randint(5, 15)
        self.color = random.choice(COLORES)
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.dx = random.randint(-5, 5)  # Velocidad en X
        self.dy = random.randint(-5, 5)  # Velocidad en Y
        self.particula = canvas.create_oval(
            self.x, self.y, self.x + self.tamaño, self.y + self.tamaño, fill=self.color
        )
