from tkinter import *
from tkinter import filedialog

def Abrir():
    filepath = filedialog.askopenfilename(initialdir='/home/misael/Documentos/Parte/prueba.txt',
                                          title='Abrir Archivo',
                                          filetypes=(('Archivo de texto','*.txt'),('Todos los archivos', '*.*')))
    archivo = open(filepath, 'r')
    print(archivo.read())
    archivo.close()

window = Tk()

boton = Button(window, text='Abri', command=Abrir)
boton.pack()

window.mainloop()
