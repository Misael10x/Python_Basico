def calcular_gas_ideal():
    R = 0.0821  
    opcion = input("¿Qué deseas calcular? (P/V/n/T): ").strip().upper()

    if opcion == "P":
        n = float(input("Introduce la cantidad de gas (moles): "))
        V = float(input("Introduce el volumen (litros): "))
        T = float(input("Introduce la temperatura (Kelvin): "))
        P = (n * R * T) / V
        print(f"\nPresión: {P} atm")
