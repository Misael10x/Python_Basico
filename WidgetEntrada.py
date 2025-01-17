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

windows = Tk()
windows.title("Gestión de Entrada")
windows.geometry("400x100")

entrada = Entry(windows, font=('Arial', 20), fg='red', bg='black', width=20)
entrada.pack(pady=10)

Button(windows, text='Enviar', command=enviar).pack(side=LEFT, padx=5)
Button(windows, text='Reset', command=reset).pack(side=LEFT, padx=5)
Button(windows, text='Delete', command=delete).pack(side=LEFT, padx=5)
