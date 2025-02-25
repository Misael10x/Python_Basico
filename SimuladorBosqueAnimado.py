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
        self.tronco = 
