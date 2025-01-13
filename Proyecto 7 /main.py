import numpy as np
import matplotlib.pyplot as plt
from fft import FFT
from ifft import IFFT
from ProcesadorAudio import procesAudio
from filtro import Filtro

def main():

    audio_entrada = "/home/verzzul/Escritorio/DAA24/Proyecto 7 /Entrada/Guitarra.mp3"
    audio_salida = "/home/verzzul/Escritorio/DAA24/Proyecto 7 /Salida/"

    datos_audio, tasa_muestreo = procesAudio.leer_audio(audio_entrada)

    datos_audio = np.array(datos_audio, dtype=float)
    datos_audio = procesAudio.rellenar_potencia(datos_audio)
    n = len(datos_audio)

    frecuencias = FFT.fft(n, datos_audio)

    magnitud = np.abs(frecuencias)
    plt.figure(figsize=(12,6))
    plt.plot("Espectro de Frecuencias (FFT)")
    plt.ylabel("Frecuencia (Hz)")
    plt.xlabel("Magnitud")
    plt.grid()
    plt.show()

    frecuencia_corte = 1000
    frecuencias_filtradas = Filtro.filtro_pasabajas(frecuencias, frecuencia_corte, tasa_muestreo)

    señal_reconstruida = IFFT.ifft(n, frecuencias_filtradas)
    señal_reconstruida = np.real(señal_reconstruida)

    procesAudio.escribir_audio(audio_salida, señal_reconstruida, tasa_muestreo)
    print(f"Archivo de audio Guardado en: {audio_salida}")

    if __name__=='__main__':
        main()