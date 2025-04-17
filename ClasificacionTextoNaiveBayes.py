import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def clasificar_texto():
    archivo = input("Archivo CSV: ")
    columna_texto = input("Nombre de la columna de texto: ")
    columna_etiqueta = input("Nombre de la columna de etiquetas: ")
