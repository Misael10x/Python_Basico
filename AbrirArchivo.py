from tkinter import *
from tkinter import filedialog

def Abrir():
    filepath = filedialog.askopenfilename(initialdir='/home/misael/Documentos/Parte/prueba.txt',
                                          title='Abrir Archivo',
                                          filetypes=(('Archivo de texto','*.txt'),('Todos los archivos', '*.*')))
