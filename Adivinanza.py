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

ventana = tk.Tk()
ventana.title("Adivina el Número")
ventana.geometry("300x150")

numero_secreto = random.randint(1, 10)

instrucciones = tk.Label(ventana, text="Adivina un número entre 1 y 10:", font=("Arial", 12))
instrucciones.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10)

boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_intento, font=("Arial", 12))
boton_verificar.pack(pady=10)

ventana.mainloop()
