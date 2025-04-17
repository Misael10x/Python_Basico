import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def clasificar_texto():
    archivo = input("Archivo CSV: ")
    columna_texto = input("Nombre de la columna de texto: ")
    columna_etiqueta = input("Nombre de la columna de etiquetas: ")

    df = pd.read_csv(archivo)
    X_train, X_test, y_train, y_test = train_test_split(df[columna_texto], df[columna_etiqueta], test_size=0.2)

    vectorizador = CountVectorizer()
    X_train_vec = vectorizador.fit_transform(X_train)
    X_test_vec = vectorizador.transform(X_test)

    modelo = MultinomialNB()
    modelo.fit(X_train_vec, y_train)
    y_pred = modelo.predict(X_test_vec)

    print("\nReporte de clasificación:")
    print(classification_report(y_test, y_pred))

if _name_ == "_main_":
    clasificar_texto()
