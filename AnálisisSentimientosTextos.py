import pandas as pd
from textblob import TextBlob

def analisis_sentimientos():
    archivo = input("Archivo CSV: ")
    columna = input("Nombre de la columna con texto: ")
    df = pd.read_csv(archivo)

    df["Polaridad"] = df[columna].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    df["Sentimiento"] = df["Polaridad"].apply(lambda p: "Positivo" if p > 0 else "Negativo" if p < 0 else "Neutro")
