import pandas as pd
from scipy import stats

def estadisticas_basicas():
    archivo = input("Nombre del archivo CSV: ")
    df = pd.read_csv(archivo)
    datos_numericos = df.select_dtypes(include='number')

    for columna in datos_numericos.columns:
        print(f"\nColumna: {columna}")
        print(f"Media: {datos_numericos[columna].mean()}")
