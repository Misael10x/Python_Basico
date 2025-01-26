from tkinter import *

def Enviar():
    input = texto.get('1.0', END)
    print(input)


window = Tk()

texto = Text(window,
             bg='#ffffe0',
             font=('Inl Free', 25),
             height=8,
             width=20,
             padx=20,
             pady=20,
             fg='red')
texto.pack()

boton = Button(window, text='Enviar', command=Enviar)
boton.pack()

window.mainloop()
