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

instrucciones = tk.Label(ventana, text="Longitud de la contraseña:", font=("Arial", 12))
instrucciones.pack(pady=10)

longitud_entry = tk.Entry(ventana, font=("Arial", 12))
longitud_entry.pack(pady=10)

boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña, font=("Arial", 12))
boton_generar.pack(pady=10)

contraseña_label = tk.Label(ventana, text="Contraseña generada: -", font=("Arial", 12))
contraseña_label.pack(pady=20)

ventana.mainloop()
