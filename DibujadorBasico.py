import tkinter as tk

def comenzar_dibujo(evento):
    global x_previo, y_previo
    x_previo, y_previo = evento.x, evento.y

def dibujar(evento):
    global x_previo, y_previo
    canvas.create_line(x_previo, y_previo, evento.x, evento.y, fill="black", width=2)
    x_previo, y_previo = evento.x, evento.y

ventana = tk.Tk()
ventana.title("Dibujador Básico")
ventana.geometry("800x600")

canvas = tk.Canvas(ventana, width=800, height=600, bg="white")
canvas.pack()

x_previo, y_previo = 0, 0

canvas.bind("<Button-1>", comenzar_dibujo)
canvas.bind("<B1-Motion>", dibujar)

ventana.mainloop()
