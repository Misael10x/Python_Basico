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
