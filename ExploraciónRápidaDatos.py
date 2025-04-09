import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def resumen_datos():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)
