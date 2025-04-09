import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def resumen_datos():
    archivo = input("Archivo CSV: ")
    df = pd.read_csv(archivo)

    print("\nResumen estadístico:")
    print(df.describe(include='all'))

    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    sns.pairplot(df.select_dtypes(include='number'))
    plt.suptitle("Relaciones entre variables numéricas", y=1.02)
    plt.tight_layout()
    plt.show()
