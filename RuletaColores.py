import tkinter as tk
import random

def girar_ruleta():
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Morado", "Rosa", "Cyan"]
    color_seleccionado = random.choice(colores)
    resultado_label.config(text=f"Color seleccionado: {color_seleccionado}", bg=color_seleccionado.lower())

ventana = tk.Tk()
ventana.title("Ruleta de Colores")
ventana.geometry("400x200")

resultado_label = tk.Label(ventana, text="Presiona 'Girar' para comenzar", font=("Arial", 18), bg="white")
resultado_label.pack(expand=True, fill="both")
