import tkinter as tk
from tkinter import messagebox
import random

def lanzar_dado():
    resultado = random.randint(1, 6)
    resultado_label.config(text=f"Resultado: {resultado}")

ventana = tk.Tk()
ventana.title("Lanzar un dado")
ventana.geometry("300x150")

resultado_label = tk.Label(ventana, text="Resultado: -", font=("Arial", 24))
resultado_label.pack(pady=20)

boton_lanzar = tk.Button(ventana, text="Lanzar dado", command=lanzar_dado, font=("Arial", 16))
boton_lanzar.pack(pady=10)

ventana.mainloop()
