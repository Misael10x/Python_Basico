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
        for _ in range(NUM_LUCES):
            luz_x = random.randint(x - 50, x + 50)
            luz_y = random.randint(y - 100, y)
            luz = canvas.create_oval(luz_x, luz_y, luz_x + 5, luz_y + 5, fill="yellow")
            self.luces.append(luz)

    def parpadear_luces(self):
        for luz in self.luces:
            if random.random() < 0.5:
                self.canvas.itemconfig(luz, fill="yellow")
            else:
                self.canvas.itemconfig(luz, fill="darkgreen")

def animar_bosque():
    for arbol in arboles:
        arbol.parpadear_luces()
    ventana.after(VELOCIDAD_PARPADEO, animar_bosque)

ventana = tk.Tk()
ventana.title("Simulador de Bosque Mágico")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

arboles = [Arbol(canvas, random.randint(100, ANCHO - 100), ALTO - 100) for _ in range(NUM_ARBOLES)]

animar_bosque()

ventana.mainloop()
