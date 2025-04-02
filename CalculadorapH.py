import math

def calcular_pH():
    H_concentracion = float(input("Introduce la concentración de iones H⁺ (mol/L): "))

    if H_concentracion <= 0:
        print("\nLa concentración debe ser mayor que cero.")
