import numpy as np
from scipy.io.wavfile import write

frecuencia = 440       # Frecuencia en Hz (La4)
duracion = 2           # Duración en segundos
tasa_muestreo = 44100  # 44.1 kHz

t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
tono = 0.5 * np.sin(2 * np.pi * frecuencia * t)

tono = np.int16(tono * 32767)
write("tono_440Hz.wav", tasa_muestreo, tono)
import numpy as np
from scipy.io.wavfile import write

frecuencia = 440       # Frecuencia en Hz (La4)
duracion = 2           # Duración en segundos
tasa_muestreo = 44100  # 44.1 kHz

t = np.linspace(0, duracion, int(tasa_muestreo * duracion), False)
