import pandas as pd
import matplotlib.pyplot as plt

def analizar_ventas():
    archivo = input("Introduce el nombre del archivo CSV: ")
    df = pd.read_csv(archivo)

    print("\nResumen general:")
    print(df.describe())
