import tkinter as tk
import random
import math

# Configuración inicial
ANCHO = 800
ALTO = 600
NUM_OLAS = 50
AMPLITUD_OLAS = 20
FRECUENCIA_OLAS = 0.02
VELOCIDAD_OLAS = 0.05

class Ola:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.angulo = random.uniform(0, 2 * math.pi)
        self.ola = canvas.create_line(x, y, x, y, fill="blue", width=2)

    def mover(self):
        self.angulo += VELOCIDAD_OLAS
        self.y = ALTO // 2 + AMPLITUD_OLAS * math.sin(FRECUENCIA_OLAS * self.x + self.angulo)
        self.canvas.coords(self.ola, self.x, self.y, self.x + 1, self.y)

def animar_rio():
    for ola in olas:
        ola.mover()
    ventana.after(30, animar_rio)
