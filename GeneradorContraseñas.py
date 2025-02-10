import tkinter as tk
from tkinter import messagebox
import random
import string

def generar_contraseña():
    try:
        longitud = int(longitud_entry.get())
        if longitud < 4:
            messagebox.showerror("Error", "La longitud mínima es 4.")
            return
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        contraseña_label.config(text=f"Contraseña generada: {contraseña}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("400x200")
