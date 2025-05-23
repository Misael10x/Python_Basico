def ley_de_velocidad():
    k = float(input("Introduce la constante de velocidad (L/mol·s): "))
    A = float(input("Introduce la concentración inicial de A (mol/L): "))
    t = float(input("Introduce el tiempo (segundos): "))

    # Ley de velocidad para una reacción de primer orden
    velocidad = k * A
    print(f"\nVelocidad de la reacción: {velocidad:.2e} mol/L·s")

if __name__ == "__main__":
    ley_de_velocidad()
