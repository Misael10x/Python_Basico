from tkinter import *

def submit():
    print("La temperatura es: " + str(scale.get()) + " grados.")

windows = Tk()

hotImage = PhotoImage(file='h.png').subsample(5, 5)
hotLabel = Label(image=hotImage)
hotLabel.pack()
