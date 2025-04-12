import pandas as pd
from scipy import stats

def estadisticas_basicas():
    archivo = input("Nombre del archivo CSV: ")
    df = pd.read_csv(archivo)
    datos_numericos = df.select_dtypes(include='number')
