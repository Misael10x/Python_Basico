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

    print(f"\nEcuación: y = {pendiente:.4f}x + {interseccion:.4f}")

    x_nuevo = float(input("Valor de X para predecir Y: "))
    y_predicho = modelo.predict([[x_nuevo]])
    print(f"Predicción: Y = {y_predicho[0]:.4f}")

if __name__ == "__main__":
    regresion_lineal()
