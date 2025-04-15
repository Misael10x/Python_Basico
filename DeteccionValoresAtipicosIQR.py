import pandas as pd

def detectar_outliers():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)
