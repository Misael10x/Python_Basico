def energia_cinetica():
    m = float(input("Introduce la masa del objeto (kg): "))
    v = float(input("Introduce la velocidad del objeto (m/s): "))
    Ec = 0.5 * m * v**2
    print(f"\nEnergía Cinética: {Ec} Joules")

if __name__ == "__main__":
    energia_cinetica()
