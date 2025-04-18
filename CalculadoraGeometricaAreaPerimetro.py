import math

def figuras_geometricas():
    print("Figuras disponibles: círculo, triángulo, cuadrado, rectángulo")
    figura = input("Elige una figura: ").lower()

    if figura == "círculo":
        r = float(input("Radio: "))
        area = math.pi * r ** 2
        perimetro = 2 * math.pi * r
