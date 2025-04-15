import pandas as pd

def detectar_outliers():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)
    numericas = df.select_dtypes(include='number')

    for columna in numericas.columns:
        q1 = numericas[columna].quantile(0.25)
        q3 = numericas[columna].quantile(0.75)
        iqr = q3 - q1
        inferior = q1 - 1.5 * iqr
        superior = q3 + 1.5 * iqr
        outliers = numericas[(numericas[columna] < inferior) | (numericas[columna] > superior)]

        print(f"\nColumna: {columna}")
        print(f"Outliers detectados: {len(outliers)}")

if __name__ == "__main__":
    detectar_outliers()
