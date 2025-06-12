from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

def analizar_sentimiento(frase):
    blob = TextBlob(frase)
    sentimiento = blob.sentiment.polarity
    if sentimiento > 0:
        print("Sentimiento positivo 😊")
    elif sentimiento < 0:
        print("Sentimiento negativo 😠")
    else:
