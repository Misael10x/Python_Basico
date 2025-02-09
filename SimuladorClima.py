import tkinter as tk
import random

def actualizar_clima():
    climas = ["Soleado ☀️", "Nublado ☁️", "Lluvioso 🌧️", "Nevado ❄️"]
    clima = random.choice(climas)
    clima_label.config(text=f"Clima actual: {clima}")

