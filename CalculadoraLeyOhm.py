def ley_de_ohm():
    opcion = input("¿Qué deseas calcular? (V/I/R): ").strip().upper()

    if opcion == "V":
        I = float(input("Introduce la corriente (A): "))
        R = float(input("Introduce la resistencia (Ω): "))
        V = I * R
