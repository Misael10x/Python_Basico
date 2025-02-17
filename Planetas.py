import tkinter as tk
import math

ANCHO = 800
ALTO = 600
CENTRO_X = ANCHO // 2
CENTRO_Y = ALTO // 2

class Planeta:
    def __init__(self, canvas, nombre, radio_orbita, radio_planeta, color, velocidad):
        self.canvas = canvas
        self.nombre = nombre
        self.radio_orbita = radio_orbita
        self.radio_planeta = radio_planeta
        self.color = color
        self.velocidad = velocidad
        self.angulo = 0
        self.planeta = canvas.create_oval(0, 0, 0, 0, fill=self.color)
        self.actualizar_posicion()

    def actualizar_posicion(self):
        self.angulo += self.velocidad
        x = CENTRO_X + self.radio_orbita * math.cos(math.radians(self.angulo))
        y = CENTRO_Y + self.radio_orbita * math.sin(math.radians(self.angulo))
        self.canvas.coords(
            self.planeta,
            x - self.radio_planeta,
            y - self.radio_planeta,
            x + self.radio_planeta,
            y + self.radio_planeta,
        )

def animar_planetas():
    for planeta in planetas:
        planeta.actualizar_posicion()
    ventana.after(30, animar_planetas)

ventana = tk.Tk()
ventana.title("Simulador del Sistema Solar")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

canvas.create_oval(CENTRO_X - 30, CENTRO_Y - 30, CENTRO_X + 30, CENTRO_Y + 30, fill="yellow")

planetas = [
    Planeta(canvas, "Mercurio", 60, 5, "gray", 2.5),
    Planeta(canvas, "Venus", 100, 8, "orange", 2.0),
    Planeta(canvas, "Tierra", 150, 10, "blue", 1.5),
    Planeta(canvas, "Marte", 200, 7, "red", 1.2),
    Planeta(canvas, "Júpiter", 280, 20, "brown", 0.8),
    Planeta(canvas, "Saturno", 360, 18, "gold", 0.6),
    Planeta(canvas, "Urano", 440, 15, "lightblue", 0.4),
    Planeta(canvas, "Neptuno", 520, 14, "darkblue", 0.3),
]

animar_planetas()
ventana.mainloop()
