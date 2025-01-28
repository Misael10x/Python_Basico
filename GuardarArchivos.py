# file dialog

from tkinter import *
from tkinter import filedialog

def Guardar():
    archivo = filedialog.asksaveasfile(initialdir='/home/misael/Documentos/Parte',
                                       defaultextension='.txt',
                                       filetypes=[
                                           ('ARchivos de texto', '.txt'),
                                           ('HTML', '.html'),
                                           ('Todos los acchivos','.*')
                                           ])
