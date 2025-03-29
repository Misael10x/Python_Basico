import math

def ley_de_coulomb():
    k = 8.99e9  
    q1 = float(input("Introduce la carga 1 (Coulombs): "))
    q2 = float(input("Introduce la carga 2 (Coulombs): "))
    r = float(input("Introduce la distancia entre las cargas (metros): "))

    if r == 0:
        print("\nLa distancia no puede ser cero.")
    else:
        F = k * (q1 * q2) / r**2
        print(f"\nFuerza electrostática: {F} Newtons")

if __name__ == "__main__":
    ley_de_coulomb()
