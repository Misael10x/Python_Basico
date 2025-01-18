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


check_button = Checkbutton(windows,
                           text='Acepto',
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=mostrar,
                           font=('Arial', 20),
                           fg='red',
                           bg='black',
                           activeforeground='red',
                           activebackground='black',
                           padx=20,
                           pady=25,
                           image=python_photo,
                           compound='left')
                
