import tkinter as tk
import random

def generar_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def iniciar_juego():
    global color_correcto
    color_correcto = generar_color()
    etiqueta_color.config(text=color_correcto)
    colores = [generar_color() for _ in range(3)]
    colores[random.randint(0, 2)] = color_correcto
    for i, boton in enumerate(botones):
        boton.config(bg=colores[i])
