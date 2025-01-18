from tkinter import *
from PIL import Image, ImageTk

def mostrar ():
    if(x.get() == 1):
        print('Estoy de acuerdo')
    else:
        print('No estas deacuerdo')

windows = Tk()


x = IntVar()

original_image = Image.open('logo.png')
resized_image = original_image.resize((50, 50)) 
python_photo = ImageTk.PhotoImage(resized_image)
