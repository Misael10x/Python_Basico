import tkinter as tk
import random

def actualizar_clima():
    climas = ["Soleado ☀️", "Nublado ☁️", "Lluvioso 🌧️", "Nevado ❄️"]
    clima = random.choice(climas)
    clima_label.config(text=f"Clima actual: {clima}")

ventana = tk.Tk()
ventana.title("Simulador de Clima")
ventana.geometry("300x150")

clima_label = tk.Label(ventana, text="Clima actual: -", font=("Arial", 18))
clima_label.pack(pady=20)

boton_actualizar = tk.Button(ventana, text="Actualizar Clima", command=actualizar_clima, font=("Arial", 14))
boton_actualizar.pack(pady=10)

ventana.mainloop()
