from tkinter import *

def click():
    print("Hicistes click en el boton")


windows = Tk()

imagen = PhotoImage(file='pulso.png')

boton = Button(windows, text='Haz click', command=click,
               font=('Arial',20,'bold'),
               fg='red',
               bg='black',
               activeforeground='red',
               activebackground='#fff',
               state='active',
               relief='raised',
               bd=10,
               padx=15,
               pady=15,
               image=imagen,
               compound='top')
boton.pack()



windows.mainloop()
