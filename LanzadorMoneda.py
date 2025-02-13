import tkinter as tk
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    resultado_label.config(text=f"Resultado: {resultado}")

window = tk.Tk()
window.title("Lanzamiento de Moneda")
window.geometry("300x150")

resultado_label = tk.Label(window, text="Resultado: -", font=("Arial", 24))
resultado_label.pack(pady=20)

boton_lanzar = tk.Button(window, text="Lanzar Moneda", command=lanzar_moneda, font=("Arial", 16))
boton_lanzar.pack(pady=10)

window.mainloop()
