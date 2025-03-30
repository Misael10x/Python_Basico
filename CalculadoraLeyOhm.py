def ley_de_ohm():
    opcion = input("¿Qué deseas calcular? (V/I/R): ").strip().upper()

    if opcion == "V":
        I = float(input("Introduce la corriente (A): "))
        R = float(input("Introduce la resistencia (Ω): "))
        V = I * R
        print(f"\nVoltaje: {V} V")
    elif opcion == "I":
        V = float(input("Introduce el voltaje (V): "))
        R = float(input("Introduce la resistencia (Ω): "))
        I = V / R
        print(f"\nCorriente: {I} A")
    elif opcion == "R":
        V = float(input("Introduce el voltaje (V): "))
        I = float(input("Introduce la corriente (A): "))
        R = V / I
        print(f"\nResistencia: {R} Ω")
    else:
        print("\nOpción no válida.")

if __name__ == "__main__":
    ley_de_ohm()
