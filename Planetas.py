import tkinter as tk
import math

# Configuración inicial
ANCHO = 800
ALTO = 600
CENTRO_X = ANCHO // 2
CENTRO_Y = ALTO // 2

# Clase para representar un planeta
class Planeta:
    def __init__(self, canvas, nombre, radio_orbita, radio_planeta, color, velocidad):
        self.canvas = canvas
        self.nombre = nombre
        self.radio_orbita = radio_orbita
        self.radio_planeta = radio_planeta
        self.color = color
        self.velocidad = velocidad
        self.angulo = 0  # Ángulo inicial de la órbita
        self.planeta = canvas.create_oval(0, 0, 0, 0, fill=self.color)
        self.actualizar_posicion()

    def actualizar_posicion(self):
        # Calcular la posición en la órbita
        self.angulo += self.velocidad
        x = CENTRO_X + self.radio_orbita * math.cos(math.radians(self.angulo))
        y = CENTRO_Y + self.radio_orbita * math.sin(math.radians(self.angulo))
        # Actualizar la posición del planeta en el canvas
        self.canvas.coords(
            self.planeta,
            x - self.radio_planeta,
            y - self.radio_planeta,
            x + self.radio_planeta,
            y + self.radio_planeta,
        )
