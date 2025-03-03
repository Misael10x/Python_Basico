import tkinter as tk
import random

def generar_color():
    return f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"

def iniciar_juego():
    global color_correcto
    color_correcto = generar_color()
    etiqueta_color.config(text=color_correcto)
    colores = [generar_color() for _ in range(3)]
    colores[random.randint(0, 2)] = color_correcto
    for i, boton in enumerate(botones):
        boton.config(bg=colores[i])

def verificar_respuesta(color_seleccionado):
    if color_seleccionado == color_correcto:
        etiqueta_resultado.config(text="¡Correcto!", fg="green")
    else:
        etiqueta_resultado.config(text="Incorrecto", fg="red")
    ventana.after(1000, iniciar_juego)

ventana = tk.Tk()
ventana.title("Juego de Adivinanza de Colores")
ventana.geometry("400x300")

etiqueta_color = tk.Label(ventana, text="", font=("Arial", 24))
etiqueta_color.pack(pady=20)

botones = []
for _ in range(3):
    boton = tk.Button(ventana, width=10, height=2, command=lambda c="": verificar_respuesta(c))
    boton.pack(pady=5)
    botones.append(boton)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 18))
etiqueta_resultado.pack(pady=20)

iniciar_juego()

ventana.mainloop()
