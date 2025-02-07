
import tkinter as tk
from tkinter import messagebox
import random

# Función para lanzar el dado
def lanzar_dado():
    resultado = random.randint(1, 6)
    resultado_label.config(text=f"Resultado: {resultado}")

