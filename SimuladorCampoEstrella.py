import tkinter as tk
import random

# Configuración inicial
ANCHO = 800
ALTO = 600
NUM_ESTRELLAS = 100
VELOCIDAD_PARPADEO = 100  # Velocidad de parpadeo en milisegundos

class Estrella:
    def _init_(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.tamaño = random.randint(1, 3)
        self.brillo = random.uniform(0.1, 1.0)
        self.estrella = canvas.create_oval(
            self.x, self.y, self.x + self.tamaño, self.y + self.tamaño, fill="white"
        )

    def parpadear(self):
        self.brillo = random.uniform(0.1, 1.0)
        color = f"#{int(255 * self.brillo):02x}{int(255 * self.brillo):02x}{int(255 * self.brillo):02x}"
        self.canvas.itemconfig(self.estrella, fill=color)
