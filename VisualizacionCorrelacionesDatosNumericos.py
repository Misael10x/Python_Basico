import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mapa_correlacion():
    archivo = input("Nombre del archivo CSV: ")
    df = pd.read_csv(archivo)
    datos_numericos = df.select_dtypes(include='number')
    
    correlaciones = datos_numericos.corr()

    print("\nMatriz de correlación:")
    print(correlaciones)

    sns.heatmap(correlaciones, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de Correlación")
    plt.tight_layout()
    plt.show()
