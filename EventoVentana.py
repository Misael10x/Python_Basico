from tkinter import *

def hacer_algo(event):
   # print('Haz presionado: '+ event.keysym)
    label.config(text=event.keysym)

window = Tk()
window.geometry('1050x200')

window.bind('<Key>',hacer_algo)

label = Label(window,font=('Helvetica',100))
label.pack()

window.mainloop()
