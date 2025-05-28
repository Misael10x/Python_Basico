import speech_recognition as sr

reconocedor = sr.Recognizer()

with sr.Microphone() as fuente:
    print("Habla algo...")
    audio = reconocedor.listen(fuente)
