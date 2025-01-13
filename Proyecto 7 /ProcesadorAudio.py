import wave
import numpy as np
from scipy.io.wavfile import write

class procesAudio:

    def leer_audio(Archivo):

        with wave.open(Archivo, "r") as archivo_wav:
            frames = archivo_wav.readframes(archivo_wav.getnframes())
            datos_audio = np.frombuffer(frames, dtype=np.int16)
            tasa_muestreo = archivo_wav.getframerate()
        return datos_audio, tasa_muestreo
    
    def escribir_audio(Archivo, datos_audio, tasa_muestreo):
        datos_audio= np.asarray(datos_audio, dtype=np.int16)
        write(Archivo, tasa_muestreo, datos_audio)
    
    def rellenar_potencia(datos):
        n = len(datos)
        if np.log2(n) % 1 > 0:
            sig_potencia = int(2 ** np.ceil(np.log2(n)))
            datos = np.pad(datos, (0,sig_potencia - n), mode='constant')
        return datos
    