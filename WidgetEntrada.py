from tkinter import *

def enviar():
    nombre_usuario = entrada.get()
    print(f"Hola {nombre_usuario}")
    entrada.config(state=DISABLED)

def reset():
    entrada.config(state=NORMAL)
    entrada.delete(0, END)

def delete():
    actual_texto = entrada.get()
    if actual_texto:
        entrada.delete(len(actual_texto) - 1, END)
