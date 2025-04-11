import pandas as pd
import matplotlib.pyplot as plt

def analisis_por_mes():
    archivo = input("Archivo CSV: ")
    columna_fecha = input("Nombre de la columna con fechas (YYYY-MM-DD): ")
    df = pd.read_csv(archivo)
