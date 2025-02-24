import tkinter as tk
import random
import math

ANCHO = 800
ALTO = 600
NUM_ONDAS = 50
AMPLITUD = 50
FRECUENCIA = 0.02
VELOCIDAD = 0.05

def generar_color_aurora():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

class Onda:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(ALTO // 2, ALTO)
        self.color = generar_color_aurora()
        self.angulo = random.uniform(0, 2 * math.pi)
        self.onda = canvas.create_line(self.x, self.y, self.x, self.y, fill=self.color, width=2)
