import tkinter as tk

ANCHO = 800
ALTO = 600
NIVELES = 5

def dibujar_sierpinski(x1, y1, x2, y2, x3, y3, nivel):
    if nivel == 0:
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="blue", outline="black")
    else:
        x12 = (x1 + x2) / 2
        y12 = (y1 + y2) / 2
        x23 = (x2 + x3) / 2
        y23 = (y2 + y3) / 2
        x31 = (x3 + x1) / 2
        y31 = (y3 + y1) / 2
        dibujar_sierpinski(x1, y1, x12, y12, x31, y31, nivel - 1)
        dibujar_sierpinski(x12, y12, x2, y2, x23, y23, nivel - 1)
        dibujar_sierpinski(x31, y31, x23, y23, x3, y3, nivel - 1)

ventana = tk.Tk()
ventana.title("Triángulo de Sierpinski")
ventana.geometry(f"{ANCHO}x{ALTO}")

canvas = tk.Canvas(ventana, width=ANCHO, height=ALTO, bg="white")
canvas.pack()

x1, y1 = ANCHO // 2, 50
x2, y2 = 50, ALTO - 50
x3, y3 = ANCHO - 50, ALTO - 50

dibujar_sierpinski(x1, y1, x2, y2, x3, y3, NIVELES)

ventana.mainloop()
