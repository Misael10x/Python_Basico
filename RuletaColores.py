import tkinter as tk
import random

def girar_ruleta():
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Morado", "Rosa", "Cyan"]
    color_seleccionado = random.choice(colores)
    resultado_label.config(text=f"Color seleccionado: {color_seleccionado}", bg=color_seleccionado.lower())
