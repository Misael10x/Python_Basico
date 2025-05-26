def contar_nucleotidos(secuencia):
    secuencia = secuencia.upper()
    conteo = {
        "A": secuencia.count("A"),
        "T": secuencia.count("T"),
        "C": secuencia.count("C"),
