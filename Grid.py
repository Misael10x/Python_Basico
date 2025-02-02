from tkinter import *

window = Tk()

tituloLabel = Label(window,text='Ingresa tu informacion', font=('Arial',25)).grid(row=0,column=0,columnspan=2)

nombreLabel = Label(window, text='Nombre: ',width=20,bg='red').grid(row=1,column=0)
nombreEntry = Entry(window).grid(row=1,column=1)
