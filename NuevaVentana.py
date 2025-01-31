from tkinter import *

def crear():
    new_window = Tk()  # con tk es una venta nueva independiente y con toplevel es una ventana dependiende de la original 
    
    window.destroy()

window = Tk()

Button(window,text='Crear nueva ventana', command=crear).pack()

window.mainloop()
