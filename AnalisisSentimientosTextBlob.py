from textblob import TextBlob

texto = input("Escribe un texto para analizar su sentimiento: ")
analisis = TextBlob(texto)

polaridad = analisis.sentiment.polarity
if polaridad > 0:
    print("Sentimiento positivo 🌞")
elif polaridad < 0:
