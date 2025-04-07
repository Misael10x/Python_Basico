import pandas as pd
import matplotlib.pyplot as plt

def analizar_ventas():
    archivo = input("Introduce el nombre del archivo CSV: ")
    df = pd.read_csv(archivo)

    print("\nResumen general:")
    print(df.describe())

    print("\nVentas totales por categoría:")
    print(df.groupby("Categoría")["Ventas"].sum())

    df.groupby("Categoría")["Ventas"].sum().plot(kind="bar", color="skyblue")
    plt.title("Ventas por Categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Ventas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    analizar_ventas()
