import tkinter as tk
import math
import random

ANCHO = 800
ALTO = 600
NUM_ESTRELLAS = 300
VELOCIDAD = 0.02

class Estrella:
    def __init__(self, canvas):
        self.canvas = canvas
        self.angulo = random.uniform(0, 2 * math.pi)
        self.distancia = random.uniform(0, ANCHO // 2)
        self.tamaño = random.uniform(1, 3)
        self.estrella = canvas.create_oval(0, 0, self.tamaño, self.tamaño, fill="white")
