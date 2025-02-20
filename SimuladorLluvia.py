import tkinter as tk
import random

ANCHO = 800
ALTO = 600
NUM_GOTAS = 100
VELOCIDAD = 5

class Gota:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(-ALTO, 0)
        self.longitud = random.randint(10, 20)
        self.gota = canvas.create_line(self.x, self.y, self.x, self.y + self.longitud, fill="blue", width=2)

    def caer(self):
        self.y += VELOCIDAD
        if self.y > ALTO:
            self.y = random.randint(-ALTO, 0)
            self.x = random.randint(0, ANCHO)
        self.canvas.coords(self.gota, self.x, self.y, self.x, self.y + self.longitud)

def animar_lluvia():
    for gota in gotas:
        gota.caer()
    ventana.after(30, animar_lluvia)

ventana = tk.Tk()
ventana.title("Simulador de Lluvia")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

gotas = [Gota(canvas) for _ in range(NUM_GOTAS)]

animar_lluvia()

ventana.mainloop()
