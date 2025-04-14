import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalizar_datos():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)
    numericas = df.select_dtypes(include='number')
