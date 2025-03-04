import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    texto = input("Escribe el texto que quieres convertir a voz: ")
    text_to_speech(texto)
