import math

def solidos_geometricos():
    print("Opciones: cubo, esfera, cilindro, cono")
    figura = input("Elige un sólido: ").lower()

    if figura == "cubo":
        lado = float(input("Lado: "))
        volumen = lado ** 3
        area = 6 * lado ** 2

    elif figura == "esfera":
        radio = float(input("Radio: "))
        volumen = (4/3) * math.pi * radio ** 3
        area = 4 * math.pi * radio ** 2

    elif figura == "cilindro":
        radio = float(input("Radio: "))
        altura = float(input("Altura: "))
        volumen = math.pi * radio ** 2 * altura
        area = 2 * math.pi * radio * (radio + altura)

    elif figura == "cono":
        radio = float(input("Radio: "))
        altura = float(input("Altura: "))
        generatriz = math.sqrt(radio**2 + altura**2)
        volumen = (1/3) * math.pi * radio ** 2 * altura
        area = math.pi * radio * (radio + generatriz)

    else:
        print("Sólido no válido.")
        return

    print(f"\nVolumen: {volumen:.2f}")
    print(f"Área superficial: {area:.2f}")

if __name__ == "__main__":
    solidos_geometricos()
