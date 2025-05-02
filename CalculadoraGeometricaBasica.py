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

def main():
    print("1. Círculo\n2. Cuadrado\n3. Triángulo")
    opcion = input("Elige una figura (1-3): ")

    if opcion == "1":
        r = float(input("Radio: "))
        a, p = circulo(r)
    elif opcion == "2":
        l = float(input("Lado: "))
        a, p = cuadrado(l)
    elif opcion == "3":
        b = float(input("Base: "))
        h = float(input("Altura: "))
        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))
        a, p = triangulo(b, h, l1, l2, l3)
    else:
        print("Opción no válida.")
        return

    print(f"Área: {a:.2f}")
    print(f"Perímetro: {p:.2f}")

if __name__ == "__main__":
    main()
