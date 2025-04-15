import pandas as pd

def detectar_outliers():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)
    numericas = df.select_dtypes(include='number')

    for columna in numericas.columns:
        q1 = numericas[columna].quantile(0.25)
        q3 = numericas[columna].quantile(0.75)
        iqr = q3 - q1
