def energia_foton():
    h = 6.626e-34  # Constante de Planck en J·s
    f = float(input("Introduce la frecuencia del fotón (Hz): "))
    E = h * f
    print(f"\nEnergía del fotón: {E:.3e} Joules")

if __name__ == "__main__":
