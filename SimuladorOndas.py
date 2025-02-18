import tkinter as tk
import math

# Configuración inicial
ANCHO = 800
ALTO = 400
AMPLITUD = 80  # Altura de las ondas
FRECUENCIA = 0.02  # Frecuencia de las ondas
VELOCIDAD = 2  # Velocidad de desplazamiento de las ondas

# Función para dibujar las ondas
def dibujar_ondas():
    canvas.delete("onda")  # Limpiar las ondas anteriores
    for x in range(ANCHO):
        y = ALTO // 2 + AMPLITUD * math.sin(FRECUENCIA * (x + desplazamiento))
        canvas.create_line(x, ALTO // 2, x, y, fill="cyan", tag="onda")
    ventana.after(30, dibujar_ondas)  # Velocidad de la animación

# Función para actualizar el desplazamiento de las ondas
def actualizar_desplazamiento():
    global desplazamiento
    desplazamiento += VELOCIDAD
    ventana.after(30, actualizar_desplazamiento)
