import pandas as pd
from scipy import stats

def estadisticas_basicas():
    archivo = input("Nombre del archivo CSV: ")
    df = pd.read_csv(archivo)
    datos_numericos = df.select_dtypes(include='number')

    for columna in datos_numericos.columns:
        print(f"\nColumna: {columna}")
        print(f"Media: {datos_numericos[columna].mean()}")
        print(f"Mediana: {datos_numericos[columna].median()}")
        print(f"Moda: {datos_numericos[columna].mode().values}")
        print(f"Desviación estándar: {datos_numericos[columna].std()}")
        print(f"Varianza: {datos_numericos[columna].var()}")
        print(f"Mínimo: {datos_numericos[columna].min()}")
        print(f"Máximo: {datos_numericos[columna].max()}")
