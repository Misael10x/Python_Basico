from tkinter import *

window = Tk()

marco = Frame(window, bg='pink', bd=5, relief=SUNKEN)
marco.pack(side=TOP)

Button(marco,text='W', font=('Consola', 25),width=3).pack(side=TOP)
Button(marco,text='A', font=('Consola', 25),width=3).pack(side=LEFT)
Button(marco,text='S', font=('Consola', 25),width=3).pack(side=LEFT)
