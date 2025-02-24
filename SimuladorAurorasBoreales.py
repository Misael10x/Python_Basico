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

    def mover(self):
        self.angulo += VELOCIDAD
        self.y = ALTO // 2 + AMPLITUD * math.sin(FRECUENCIA * self.x + self.angulo)
        self.canvas.coords(self.onda, self.x, self.y, self.x + 1, self.y)

def animar_auroras():
    for onda in ondas:
        onda.mover()
    ventana.after(30, animar_auroras)

ventana = tk.Tk()
ventana.title("Simulador de Auroras Boreales")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

ondas = [Onda(canvas) for _ in range(NUM_ONDAS)]

animar_auroras()

ventana.mainloop()
