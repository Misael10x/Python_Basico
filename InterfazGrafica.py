from tkinter import *
from PIL import Image, ImageTk

windows = Tk()

windows.geometry("600x600")
windows.title('Bienvenido al mundo de la Programacion con Python')

try:
    img = Image.open('logo2.png')  
    icono = ImageTk.PhotoImage(img)  
    windows.iconphoto(True, icono)
except Exception as e:
    print("Error al cargar la imagen:", e)

windows.config(background='purple')

windows.mainloop()
