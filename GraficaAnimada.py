import tkinter as tk
import random

categorias = ["Ventas", "Marketing", "Desarrollo", "Soporte", "Finanzas"]
colores = ["#FF5733", "#33FF57", "#3357FF", "#F333FF", "#FFC300"]
valores = [random.randint(10, 100) for _ in categorias]

def animar_barras():
    for i, barra in enumerate(barras):
        nuevo_valor = random.randint(10, 100)
        incremento = 1 if nuevo_valor > valores[i] else -1
        while valores[i] != nuevo_valor:
            valores[i] += incremento
            canvas.coords(barra, 50 + i * 120, 250 - valores[i], 150 + i * 120, 250)
            ventana.update()
            ventana.after(10)
    ventana.after(1000, animar_barras)

ventana = tk.Tk()
ventana.title("Gráfico de Barras Animado")
ventana.geometry("800x400")

canvas = tk.Canvas(ventana, width=800, height=300, bg="#F0F0F0")
canvas.pack(pady=20)

barras = []
for i, (categoria, valor) in enumerate(zip(categorias, valores)):
    x0 = 50 + i * 120
    y0 = 250 - valor
    x1 = 150 + i * 120
    y1 = 250
    barra = canvas.create_rectangle(x0, y0, x1, y1, fill=colores[i])
    barras.append(barra)
    canvas.create_text(x0 + 50, 260, text=categoria, font=("Arial", 12), fill="black")

animar_barras()

ventana.mainloop()
