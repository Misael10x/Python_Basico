import math

def figuras_geometricas():
    print("Figuras disponibles: círculo, triángulo, cuadrado, rectángulo")
    figura = input("Elige una figura: ").lower()

    if figura == "círculo":
        r = float(input("Radio: "))
        area = math.pi * r ** 2
        perimetro = 2 * math.pi * r

    elif figura == "triángulo":
        a = float(input("Lado 1: "))
        b = float(input("Lado 2: "))
        c = float(input("Lado 3: "))
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimetro = a + b + c
