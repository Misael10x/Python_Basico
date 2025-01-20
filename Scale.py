from tkinter import *

def submit():
    print("La temperatura es: " + str(scale.get()) + " grados.")

windows = Tk()

hotImage = PhotoImage(file='h.png').subsample(5, 5)
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(windows,
              from_=100,
              to=0,
              font='Arial',
              length=500,
              orient=VERTICAL,
              tickinterval=10,
              #showvalue=0,
              resolution=5,
              troughcolor='#ff6600',
              fg='#ff1c00',
              bg='#111111')
scale.set(((scale['from'] - scale['to']) / 2) + scale['to'])
scale.pack()

coldImage = PhotoImage(file='hielo.png').subsample(15, 15)
coldLabel = Label(image=coldImage)
coldLabel.pack()

boton = Button(windows, text='Enviar', command=submit)
boton.pack()

windows.mainloop()
