def ley_de_velocidad():
    k = float(input("Introduce la constante de velocidad (L/mol·s): "))
    A = float(input("Introduce la concentración inicial de A (mol/L): "))
    t = float(input("Introduce el tiempo (segundos): "))

    # Ley de velocidad para una reacción de primer orden
    velocidad = k * A
