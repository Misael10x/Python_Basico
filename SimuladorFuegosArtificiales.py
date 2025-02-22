import tkinter as tk
import random
import math

ANCHO = 800
ALTO = 600
NUM_PARTICULAS = 100
GRAVEDAD = 0.1

class Particula:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.angulo = random.uniform(0, 2 * math.pi)
        self.velocidad = random.uniform(1, 5)
        self.tiempo_vida = random.randint(50, 100)
        self.particula = canvas.create_oval(x, y, x + 5, y + 5, fill=self.color)

    def mover(self):
        self.velocidad -= GRAVEDAD
        self.x += self.velocidad * math.cos(self.angulo)
        self.y += self.velocidad * math.sin(self.angulo)
        self.tiempo_vida -= 1
        self.canvas.move(self.particula, self.velocidad * math.cos(self.angulo), self.velocidad * math.sin(self.angulo))

def crear_fuego_artificial():
    x = random.randint(100, ANCHO - 100)
    y = random.randint(100, ALTO - 100)
    color = random.choice(["red", "green", "blue", "yellow", "cyan", "magenta", "orange"])
    for _ in range(NUM_PARTICULAS):
        particulas.append(Particula(canvas, x, y, color))
    ventana.after(random.randint(500, 1500), crear_fuego_artificial)

def animar_particulas():
    for particula in particulas[:]:
        particula.mover()
        if particula.tiempo_vida <= 0:
            canvas.delete(particula.particula)
            particulas.remove(particula)
    ventana.after(30, animar_particulas)

