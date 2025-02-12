import tkinter as tk
from time import strftime

def actualizar_hora():
    hora_actual = strftime("%H:%M:%S %p")
    etiqueta_hora.config(text=hora_actual)
    etiqueta_hora.after(1000, actualizar_hora) 
