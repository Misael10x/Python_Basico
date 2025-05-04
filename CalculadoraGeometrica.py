import math

def area_perimetro_circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def area_perimetro_cuadrado(lado):
    area = lado**2
    perimetro = 4 * lado
    return area, perimetro

def area_perimetro_triangulo(base, altura, lado1, lado2):
    area = 0.5 * base * altura
    perimetro = base + lado1 + lado2
    return area, perimetro

opcion = input("¿Qué figura quieres calcular? (circulo/cuadrado/triangulo): ").lower()

if opcion == "circulo":
    r = float(input("Ingresa el radio: "))
    a, p = area_perimetro_circulo(r)
elif opcion == "cuadrado":
    l = float(input("Ingresa el lado: "))
    a, p = area_perimetro_cuadrado(l)
elif opcion == "triangulo":
    b = float(input("Ingresa la base: "))
    h = float(input("Ingresa la altura: "))
    l1 = float(input("Ingresa el lado 1: "))
    l2 = float(input("Ingresa el lado 2: "))
    a, p = area_perimetro_triangulo(b, h, l1, l2)
else:
    print("Figura no válida.")
    exit()

print("Área:", round(a, 2))
print("Perímetro:", round(p, 2))
