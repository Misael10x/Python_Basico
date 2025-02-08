import tkinter as tk
import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    resultado_label.config(text=f"Resultado: {dado1} + {dado2} = {suma}")
