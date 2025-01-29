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
