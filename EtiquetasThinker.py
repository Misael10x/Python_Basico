from tkinter import *

Window = Tk()

Label = Label(Window, text='Hola, Bienvenido Misael :)',
              font=('Arial',40,'bold'),
              fg='green',
              bg='black',
              relief='groove',
              bd=20,
              padx=50,
              pady=50)
Label.pack(padx=150, pady=150)
#Label.place(x=100, y=100)
