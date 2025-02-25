import tkinter as tk
import random
import math

ANCHO = 800
ALTO = 600
NUM_ARBOLES = 10
VELOCIDAD_VIENTO = 0.05
AMPLITUD_VIENTO = 10

class Arbol:
    def _init_(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tronco = canvas.create_rectangle(x - 10, y, x + 10, y + 100, fill="brown")
        self.copa = canvas.create_oval(x - 50, y - 100, x + 50, y, fill="green")
        self.hojas = []
        for _ in range(20):
            hoja_x = random.randint(x - 50, x + 50)
            hoja_y = random.randint(y - 100, y)
            hoja = canvas.create_oval(hoja_x, hoja_y, hoja_x + 5, hoja_y + 5, fill="lightgreen")
            self.hojas.append(hoja)

    def mover_hojas(self, angulo):
        for hoja in self.hojas:
            coords = self.canvas.coords(hoja)
            dx = AMPLITUD_VIENTO * math.sin(angulo)
            self.canvas.move(hoja, dx, 0)

def animar_bosque():
    angulo = 0
    while True:
        angulo += VELOCIDAD_VIENTO
        for arbol in arboles:
            arbol.mover_hojas(angulo)
        ventana.update()
        ventana.after(30)

ventana = tk.Tk()
ventana.title("Simulador de Bosque Animado")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="lightblue")
canvas.pack()

arboles = [Arbol(canvas, random.randint(100, ANCHO - 100), ALTO - 100) for _ in range(NUM_ARBOLES)]

animar_bosque()

ventana.mainloop()
