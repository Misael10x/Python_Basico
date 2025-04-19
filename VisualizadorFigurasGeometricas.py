import turtle

def dibujar_figura():
    print("Figuras: cuadrado, triángulo, círculo")
    figura = input("Elige figura: ").lower()
    t = turtle.Turtle()

    if figura == "cuadrado":
        lado = int(input("Lado: "))
        for _ in range(4):
            t.forward(lado)
            t.right(90)

    elif figura == "triángulo":
        lado = int(input("Lado: "))
        for _ in range(3):
            t.forward(lado)
            t.left(120)

    elif figura == "círculo":
        radio = int(input("Radio: "))
        t.circle(radio)

    else:
        print("Figura no válida.")
        turtle.bye()

    turtle.done()

if __name__ == "__main__":
    dibujar_figura()
