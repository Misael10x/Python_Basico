import pandas as pd
from textblob import TextBlob

def analisis_sentimientos():
    archivo = input("Archivo CSV: ")
    columna = input("Nombre de la columna con texto: ")
    df = pd.read_csv(archivo)
