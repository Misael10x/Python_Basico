import tkinter as tk
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    resultado_label.config(text=f"Resultado: {dado1} + {dado2} = {suma}")

ventana = tk.Tk()
ventana.title("Juego de Dados")
ventana.geometry("400x200")

resultado_label = tk.Label(ventana, text="Resultado: -", font=("Arial", 24))
resultado_label.pack(pady=20)

boton_lanzar = tk.Button(ventana, text="Lanzar dados", command=lanzar_dados, font=("Arial", 16))
boton_lanzar.pack(pady=10)

ventana.mainloop()
