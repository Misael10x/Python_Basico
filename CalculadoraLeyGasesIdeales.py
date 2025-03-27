def calcular_gas_ideal():
    R = 0.0821  
    opcion = input("¿Qué deseas calcular? (P/V/n/T): ").strip().upper()

    if opcion == "P":
        n = float(input("Introduce la cantidad de gas (moles): "))
        V = float(input("Introduce el volumen (litros): "))
        T = float(input("Introduce la temperatura (Kelvin): "))
        P = (n * R * T) / V
        print(f"\nPresión: {P} atm")
    elif opcion == "V":
        n = float(input("Introduce la cantidad de gas (moles): "))
        P = float(input("Introduce la presión (atm): "))
        T = float(input("Introduce la temperatura (Kelvin): "))
        V = (n * R * T) / P
        print(f"\nVolumen: {V} litros")
    elif opcion == "N":
        P = float(input("Introduce la presión (atm): "))
        V = float(input("Introduce el volumen (litros): "))
        T = float(input("Introduce la temperatura (Kelvin): "))
        n = (P * V) / (R * T)
        print(f"\nCantidad de gas: {n} moles")
    elif opcion == "T":
        n = float(input("Introduce la cantidad de gas (moles): "))
        P = float(input("Introduce la presión (atm): "))
        V = float(input("Introduce el volumen (litros): "))
        T = (P * V) / (n * R)
        print(f"\nTemperatura: {T} Kelvin")
    else:
        print("\nOpción no válida.")
