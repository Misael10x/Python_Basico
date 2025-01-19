from tkinter import *
from PIL import Image, ImageTk

comida = ['Pizza', 'Hamburguesa', 'Hotdog']

def orden():
    if x.get() == 0:
        print('Haz ordenado una Pizza')
    elif x.get() == 1:
        print('Haz ordenado una Hamburguesa')
    elif x.get() == 2:
        print('Haz ordenado un Hotdog')
    else:
        print('ERROR')
