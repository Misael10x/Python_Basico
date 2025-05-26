def contar_nucleotidos(secuencia):
    secuencia = secuencia.upper()
    conteo = {
        "A": secuencia.count("A"),
        "T": secuencia.count("T"),
        "C": secuencia.count("C"),
        "G": secuencia.count("G")
    }
    return conteo

adn = input("Introduce la secuencia de ADN: ")
resultado = contar_nucleotidos(adn)

for base, cantidad in resultado.items():
    print(f"{base}: {cantidad}")
