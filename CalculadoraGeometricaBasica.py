
import math
def circulo(radio):
    area = math.pi * radio**2
    perimetro = 2 * math.pi * radio
    return area, perimetro
def cuadrado(lado):
    area = lado**2
    perimetro = 4 * lado
    return area, perimetro
def triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro
def triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro
def main():
    print("1. Círculo\n2. Cuadrado\n3. Triángulo")
    opcion = input("Elige una figura (1-3): ")
