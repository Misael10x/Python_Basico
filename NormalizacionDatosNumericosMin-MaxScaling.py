import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalizar_datos():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)
    numericas = df.select_dtypes(include='number')
    
    scaler = MinMaxScaler()
    datos_normalizados = scaler.fit_transform(numericas)
    df_normalizado = pd.DataFrame(datos_normalizados, columns=numericas.columns)

    print("\nDatos normalizados entre 0 y 1:")
    print(df_normalizado.head())

if __name__ == "__main__":
    normalizar_datos()
