import tkinter as tk
import math

ANCHO = 800
ALTO = 400
AMPLITUD = 80
FRECUENCIA = 0.02
VELOCIDAD = 2

def dibujar_ondas():
    canvas.delete("onda")
    for x in range(ANCHO):
        y = ALTO // 2 + AMPLITUD * math.sin(FRECUENCIA * (x + desplazamiento))
        canvas.create_line(x, ALTO // 2, x, y, fill="cyan", tag="onda")
    ventana.after(30, dibujar_ondas)

def actualizar_desplazamiento():
    global desplazamiento
    desplazamiento += VELOCIDAD
    ventana.after(30, actualizar_desplazamiento)

ventana = tk.Tk()
ventana.title("Simulador de Ondas de Sonido")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="black")
canvas.pack()

desplazamiento = 0

dibujar_ondas()
actualizar_desplazamiento()

ventana.mainloop()
