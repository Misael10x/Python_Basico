def energia_potencial():
    m = float(input("Introduce la masa del objeto (kg): "))
    h = float(input("Introduce la altura (m): "))
    g = 9.81  

    Ep = m * g * h
    print(f"\nEnergía Potencial Gravitatoria: {Ep:.2f} Joules")

if __name__ == "__main__":
    energia_potencial()
