import math

def calcular_pH():
    H_concentracion = float(input("Introduce la concentración de iones H⁺ (mol/L): "))

    if H_concentracion <= 0:
        print("\nLa concentración debe ser mayor que cero.")
    else:
        pH = -math.log10(H_concentracion)
        print(f"\nEl pH de la solución es: {pH:.2f}")

if __name__ == "__main__":
    calcular_pH()
