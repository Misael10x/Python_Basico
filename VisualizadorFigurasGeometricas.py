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
