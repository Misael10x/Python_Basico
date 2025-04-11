import pandas as pd
import matplotlib.pyplot as plt

def analisis_por_mes():
    archivo = input("Archivo CSV: ")
    columna_fecha = input("Nombre de la columna con fechas (YYYY-MM-DD): ")
    df = pd.read_csv(archivo)

    df[columna_fecha] = pd.to_datetime(df[columna_fecha], errors='coerce')
    df["Mes"] = df[columna_fecha].dt.to_period("M")
    
    conteo_mensual = df["Mes"].value_counts().sort_index()
    print("\nCantidad de registros por mes:")
    print(conteo_mensual)

    conteo_mensual.plot(kind="bar", color="orange")
    plt.title("Registros por Mes")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
