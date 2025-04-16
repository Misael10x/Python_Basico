import pandas as pd
from sklearn.linear_model import LinearRegression

def regresion_lineal():
    archivo = input("Archivo CSV: ")
    columna_x = input("Columna X: ")
    columna_y = input("Columna Y: ")

    df = pd.read_csv(archivo)
    X = df[[columna_x]]
    y = df[columna_y]

    modelo = LinearRegression()
    modelo.fit(X, y)

    pendiente = modelo.coef_[0]
    interseccion = modelo.intercept_
