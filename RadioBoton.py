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

def cargar_imagen(ruta, ancho, alto):
    imagen = Image.open(ruta)
    imagen = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(imagen)

windows = Tk()

pizzaImage = cargar_imagen('pizza.png', 100, 100)
hamburgerImage = cargar_imagen('hamburguesa.png', 100, 100)
hotdogImage = cargar_imagen('hotdog.png', 100, 100)
foodImage = [pizzaImage, hamburgerImage, hotdogImage]


x = IntVar()

for index in range(len(comida)):
    radiobutton = Radiobutton(windows,
                              text=comida[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Arial', 20),
                              image=foodImage[index],
                              compound='left',
                              indicatoron=0,
                              width=400,
                              command=orden)
    radiobutton.pack(anchor=W)


windows.mainloop()
