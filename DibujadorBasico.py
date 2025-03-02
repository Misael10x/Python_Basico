import tkinter as tk

def comenzar_dibujo(evento):
    global x_previo, y_previo
    x_previo, y_previo = evento.x, evento.y
