
import statistics
def analisis(lista):
    media = statistics.mean(lista)
    mediana = statistics.median(lista)
    desviacion = statistics.stdev(lista) if len(lista) > 1 else 0
    minimo = min(lista)
    maximo = max(lista)
    return media, mediana, desviacion, minimo, maximo
