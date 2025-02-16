import tkinter as tk
import random

ANCHO = 800
ALTO = 600
NUM_PARTICULAS = 50  
COLORES = ["red", "green", "blue", "yellow", "cyan", "magenta", "orange"]

class Particula:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tamaño = random.randint(5, 15)
        self.color = random.choice(COLORES)
        self.x = random.randint(0, ANCHO)
        self.y = random.randint(0, ALTO)
        self.dx = random.randint(-5, 5)
        self.dy = random.randint(-5, 5)
        self.particula = canvas.create_oval(
            self.x, self.y, self.x + self.tamaño, self.y + self.tamaño, fill=self.color
        )

    def mover(self):
        self.x += self.dx
        self.y += self.dy
        if self.x <= 0 or self.x + self.tamaño >= ANCHO:
            self.dx *= -1
        if self.y <= 0 or self.y + self.tamaño >= ALTO:
            self.dy *= -1
        self.canvas.move(self.particula, self.dx, self.dy)

def animar_particulas():
    for particula in particulas:
        particula.mover()
    ventana.after(30, animar_particulas)

ventana = tk.Tk()
ventana.title("Simulador de Partículas")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

particulas = [Particula(canvas) for _ in range(NUM_PARTICULAS)]

animar_particulas()

ventana.mainloop()
