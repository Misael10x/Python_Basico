from tkinter import *
from tkinter.ttk import *
import time

def start():
    print('Descargando...')
    GB = 100
    dowload = 0
    speed = 0.5
    while(dowload<GB):
        time.sleep(0.05)
        bar['value']+= (speed/GB)*100
        dowload+= speed
        porcentaje.set(str(int((dowload/GB))*100)+'%')
        texto.set(str(dowload)+'/'+str(GB)+ 'GB Completado')
        window.update_idletasks()


window = Tk()
porcentaje = StringVar()
texto = StringVar()
