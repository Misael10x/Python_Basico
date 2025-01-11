from tkinter import * 

windows = Tk()

windows.geometry("600x600")

windows.title('Bienvenido al mundo de la Programacion conm Python')

icono = PhotoImage(file='logo2.png')
windows.iconphoto(True, icono)
windows.config(background='purple')


windows.mainloop()
