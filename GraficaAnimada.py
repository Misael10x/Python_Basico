import tkinter as tk
import random

# Configuración inicial
categorias = ["Ventas", "Marketing", "Desarrollo", "Soporte", "Finanzas"]
colores = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FFC300"]
valores = [random.randint(10, 100) for _ in categorias]  # Valores iniciales aleatorios

# Función para animar las barras
def animar_barras():
    for i, barra in enumerate(barras):
        nuevo_valor = random.randint(10, 100)  # Nuevo valor aleatorio
        incremento = 1 if nuevo_valor > valores[i] else -1  # Dirección de la animación
        while valores[i] != nuevo_valor:
            valores[i] += incremento
            canvas.coords(barra, 50 + i * 120, 250 - valores[i], 150 + i * 120, 250)
            ventana.update()
            ventana.after(10)  # Velocidad de la animación
    ventana.after(1000, animar_barras)  # Repetir la animación
