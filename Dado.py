import tkinter as tk
from tkinter import messagebox
import random

# Función para lanzar el dado
def lanzar_dado():
    resultado = random.randint(1, 6)
    resultado_label.config(text=f"Resultado: {resultado}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lanzar un dado")
ventana.geometry("300x150")

