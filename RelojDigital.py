import tkinter as tk
from time import strftime

def actualizar_hora():
    hora_actual = strftime("%H:%M:%S %p")
    etiqueta_hora.config(text=hora_actual)
    etiqueta_hora.after(1000, actualizar_hora) 
window = tk.Tk()
window.title("Reloj Digital")
window.geometry("300x150")

etiqueta_hora = tk.Label(window, font=("Arial", 40), background="black", foreground="white")
etiqueta_hora.pack(expand=True)

actualizar_hora()

window.mainloop()
