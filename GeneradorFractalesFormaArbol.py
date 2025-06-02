import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("black")

rama = turtle.Turtle()
rama.color("lime")
rama.left(90)
rama.speed(0)

def arbol(longitud):
    if longitud < 10:
        return
    rama.forward(longitud)
    rama.left(30)
    arbol(longitud - 10)
    rama.right(60)
    arbol(longitud - 10)
    rama.left(30)
    rama.backward(longitud)

arbol(100)
pantalla.mainloop()
