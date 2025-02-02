from tkinter import *

window = Tk()

tituloLabel = Label(window,text='Ingresa tu informacion', font=('Arial',25)).grid(row=0,column=0,columnspan=2)

nombreLabel = Label(window, text='Nombre: ',width=20,bg='red').grid(row=1,column=0)
nombreEntry = Entry(window).grid(row=1,column=1)

apelliodoLabel = Label(window, text='Apellido: ',width=20,bg='blue').grid(row=2,column=0)
apellidoEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window, text='Email: ',width=20,bg='green').grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)
