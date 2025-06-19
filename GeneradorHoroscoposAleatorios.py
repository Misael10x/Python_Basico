import random

signos = [
    "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo",
    "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"
]

mensajes = [
    "Hoy es un buen día para comenzar algo nuevo.",
    "Evita discusiones innecesarias.",
    "Alguien cercano te dará una sorpresa.",
    "Confía en tu intuición.",
    "El universo te está guiando hacia algo importante.",
    "Tómate un tiempo para descansar.",
    "Tus esfuerzos serán recompensados pronto.",
    "Mantén la calma ante los imprevistos.",
    "Recibirás buenas noticias inesperadas.",
    "Hoy es un buen día para perdonar y soltar."
]

signo = input("¿Cuál es tu signo zodiacal?: ").capitalize()

if signo in signos:
    print(f"Horóscopo para {signo}: {random.choice(mensajes)}")
else:
    print("Ese signo no es válido. Verifica la ortografía.")
