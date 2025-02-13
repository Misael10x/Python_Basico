import tkinter as tk
import random

def lanzar_moneda():
    resultado = random.choice(["Cara", "Cruz"])
    resultado_label.config(text=f"Resultado: {resultado}")
