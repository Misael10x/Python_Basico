from tkinter import *

def abrir():
    print('Abriendo archivo')
def guardar():
    print('Guardando......')
def cortar():
    print('Cortando......')
def copiar():
    print('Copiando......')
def pegar():
    print('Pegando......')

window = Tk()

openImage = PhotoImage(file='open.png').subsample(20,20)
saveImage = PhotoImage(file='sa.png').subsample(25,25)
exitImage = PhotoImage(file='ex.png').subsample(40,40)

menubar= Menu(window)                                   
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0,font=('MV Boli', 25))
menubar.add_cascade(label='Archivos', menu=fileMenu)
fileMenu.add_command(label='Abrir',command=abrir, image=openImage, compound='left')
fileMenu.add_command(label='Guardar',command=guardar, image=saveImage, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Salir',command=quit, image=exitImage,compound='left')
