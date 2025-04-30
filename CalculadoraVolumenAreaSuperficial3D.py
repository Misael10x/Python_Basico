import math

def esfera(r):
    volumen = (4/3) * math.pi * r**3
    area = 4 * math.pi * r**2
    return volumen, area

def cubo(lado):
    volumen = lado ** 3
    area = 6 * lado ** 2
    return volumen, area

def cilindro(r, h):
    volumen = math.pi * r**2 * h
    area = 2 * math.pi * r * (r + h)
    return volumen, area

def main():
    print("Calculadora de Volumen y Área Superficial")
    print("1. Esfera\n2. Cubo\n3. Cilindro")
    opcion = input("Selecciona una figura (1/2/3): ")

    if opcion == "1":
        r = float(input("Radio de la esfera: "))
        v, a = esfera(r)
    elif opcion == "2":
        lado = float(input("Lado del cubo: "))
        v, a = cubo(lado)
    elif opcion == "3":
        r = float(input("Radio del cilindro: "))
        h = float(input("Altura del cilindro: "))
        v, a = cilindro(r, h)
    else:
        print("Opción inválida")
        return

    print(f"Volumen: {v:.2f}")
    print(f"Área superficial: {a:.2f}")

if __name__ == "__main__":
    main()
