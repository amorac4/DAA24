import os
import numpy as np
import matplotlib.pyplot as plt
from fft import FFT
from ifft import IFFT
from ProcesadorAudio import procesAudio
from filtro import Filtro

def main():
    # Rutas de archivos
    audio_entrada = "/home/verzzul/Escritorio/DAA24/Proyecto 7 /Entrada/Guitarra.mp3"
    audio_salida = "/home/verzzul/Escritorio/DAA24/Proyecto 7 /Salida/Guitarra_filtrada.wav"

    # Verificar existencia del archivo de entrada
    if not os.path.exists(audio_entrada):
        print(f"Error: El archivo {audio_entrada} no existe.")
        return

    # Crear directorio de salida si no existe
    os.makedirs(os.path.dirname(audio_salida), exist_ok=True)

    # Verificar formato del archivo de entrada y convertir si es necesario
    if audio_entrada.endswith(".mp3"):
        ruta_temporal = audio_entrada.replace(".mp3", ".wav")
        procesAudio.convertir_mp3_a_wav(audio_entrada, ruta_temporal)
        audio_entrada = ruta_temporal
    else:
        ruta_temporal = None

    # Leer archivo de audio
    datos_audio, tasa_muestreo = procesAudio.leer_audio(audio_entrada)

    # Preparar datos: convertir a float y rellenar si es necesario
    datos_audio = np.array(datos_audio, dtype=float)
    datos_audio = procesAudio.rellenar_potencia(datos_audio)
    n = len(datos_audio)

    # Realizar la FFT
    frecuencias = FFT.fft(n, datos_audio)

    # Graficar las frecuencias
    magnitud = np.abs(frecuencias)
    plt.figure(figsize=(12, 6))
    plt.plot(magnitud)
    plt.title("Espectro de Frecuencias (FFT)")
    plt.xlabel("Frecuencia (Hz)")
    plt.ylabel("Magnitud")
    plt.grid()
    plt.show()

    # Aplicar filtro pasabajas
    frecuencia_corte = 1000  # Frecuencia de corte en Hz
    frecuencias_filtradas = Filtro.filtro_pasabajas(frecuencias, frecuencia_corte, tasa_muestreo)

    # Reconstruir señal con la IFFT
    señal_reconstruida = IFFT.ifft(n, frecuencias_filtradas)
    señal_reconstruida = np.real(señal_reconstruida)

    # Guardar la señal reconstruida
    procesAudio.escribir_audio(audio_salida, señal_reconstruida, tasa_muestreo)
    print(f"Archivo de audio filtrado guardado en: {audio_salida}")

    # Eliminar archivo temporal si se creó
    if ruta_temporal and os.path.exists(ruta_temporal):
        os.remove(ruta_temporal)

if __name__ == '__main__':
    main()
