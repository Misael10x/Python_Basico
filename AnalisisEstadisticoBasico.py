import statistics

def analisis(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    desviacion = statistics.stdev(lista) if len(lista) > 1 else 0
    minimo = min(lista)
    maximo = max(lista)
    return media, mediana, desviacion, minimo, maximo

def main():
    entrada = input("Introduce números separados por comas: ")
    datos = [float(n) for n in entrada.split(",")]
    media, mediana, desv, mini, maxi = analisis(datos)

    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {desv:.2f}")
    print(f"Mínimo: {mini}")
    print(f"Máximo: {maxi}")

if __name__ == "__main__":
    main()
