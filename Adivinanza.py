import tkinter as tk
from tkinter import messagebox
import random

def verificar_intento():
    try:
        numero_usuario = int(entrada.get())
        if numero_usuario == numero_secreto:
            messagebox.showinfo("Resultado", "¡Correcto! Adivinaste el número.")
        else:
            messagebox.showinfo("Resultado", f"Incorrecto. El número era {numero_secreto}.")
        reiniciar_juego()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

def reiniciar_juego():
    global numero_secreto
    numero_secreto = random.randint(1, 10)
    entrada.delete(0, tk.END)
