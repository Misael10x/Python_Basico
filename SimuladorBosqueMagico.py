import tkinter as tk
import random

ANCHO = 800
ALTO = 600
NUM_ARBOLES = 10
NUM_LUCES = 20
VELOCIDAD_PARPADEO = 200

class Arbol:
    def _init_(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.tronco = canvas.create_rectangle(x - 10, y, x + 10, y + 100, fill="brown")
        self.copa = canvas.create_oval(x - 50, y - 100, x + 50, y, fill="darkgreen")
        self.luces = []
