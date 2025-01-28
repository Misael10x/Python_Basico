# file dialog

from tkinter import *
from tkinter import filedialog

def Guardar():
    archivo = filedialog.asksaveasfile(initialdir='/home/misael/Documentos/Parte',
                                       defaultextension='.txt',
                                       filetypes=[
                                           ('Archivos de texto', '.txt'),
                                           ('HTML', '.html'),
                                           ('Todos los acchivos','.*')
                                           ])
    if archivo is None:
        return
    archivoTexto = texto.get(1.0, END)
    archivo.write(archivoTexto)
    archivo.close()
    
window = Tk()

boton = Button(window, text='Guardar', command=Guardar)
boton.pack()
texto = Text(window)
texto.pack()

window.mainloop()
