import wave
import numpy as np
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

class procesAudio:
    # Leer archivo en .wav
    def leer_audio(Archivo):
        with wave.open(Archivo, "r") as archivo_wav:
            frames = archivo_wav.readframes(archivo_wav.getnframes())
            datos_audio = np.frombuffer(frames, dtype=np.int16)
            tasa_muestreo = archivo_wav.getframerate()
        return datos_audio, tasa_muestreo

    # Escribir archivo en .wav
    def escribir_audio(Archivo, datos_audio, tasa_muestreo):
        datos_audio = np.asarray(datos_audio, dtype=np.int16)
        write(Archivo, tasa_muestreo, datos_audio)

    # Rellena la señal para que la longitud sea potencia de 2
    def rellenar_potencia(datos):
        if len(datos) == 0:
            raise ValueError("Los datos están vacíos y no se pueden rellenar.")
        n = len(datos)
        if np.log2(n) % 1 > 0:
            sig_potencia = int(2 ** np.ceil(np.log2(n)))
            datos = np.pad(datos, (0, sig_potencia - n), mode='constant')
        return datos

    # Convierte un archivo .mp3 a .wav
    def convertir_mp3_a_wav(ruta_mp3, ruta_wav):
        try:
            audio = AudioSegment.from_mp3(ruta_mp3)
            audio.export(ruta_wav, format="wav")
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo MP3: {ruta_mp3}")
        except Exception as e:
            raise ValueError(f"Error al convertir {ruta_mp3} a .wav. Detalles: {e}")
