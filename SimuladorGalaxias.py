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

    def mover(self):
        self.angulo += VELOCIDAD
        self.distancia += 0.1  # Expansión gradual de la espiral
        x = ANCHO // 2 + self.distancia * math.cos(self.angulo)
        y = ALTO // 2 + self.distancia * math.sin(self.angulo)
        self.canvas.coords(self.estrella, x, y, x + self.tamaño, y + self.tamaño)

def animar_galaxia():
    for estrella in estrellas:
        estrella.mover()
    ventana.after(30, animar_galaxia)

ventana = tk.Tk()
ventana.title("Simulador de Galaxia en Espiral")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

estrellas = [Estrella(canvas) for _ in range(NUM_ESTRELLAS)]

animar_galaxia()

ventana.mainloop()
