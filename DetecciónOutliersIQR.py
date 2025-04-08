import pandas as pd

def detectar_outliers():
    archivo = input("Nombre del archivo CSV: ")
    columna = input("Nombre de la columna numérica a analizar: ")
    df = pd.read_csv(archivo)

    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
