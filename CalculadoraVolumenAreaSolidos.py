import math

def solidos_geometricos():
    print("Opciones: cubo, esfera, cilindro, cono")
    figura = input("Elige un sólido: ").lower()

    if figura == "cubo":
        lado = float(input("Lado: "))
        volumen = lado ** 3
        area = 6 * lado ** 2
