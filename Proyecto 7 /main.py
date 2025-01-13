from pydub import AudioSegment
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
    audio_salida_wav = "/home/verzzul/Escritorio/DAA24/Proyecto 7 /Salida/Guitarra_filtrada.wav"
    audio_salida_mp3 = "/home/verzzul/Escritorio/DAA24/Proyecto 7 /Salida/Guitarra_filtrada.mp3"

    try:
        # Verificar existencia del archivo de entrada
        if not os.path.exists(audio_entrada):
            raise FileNotFoundError(f"El archivo de entrada no existe: {audio_entrada}")

        # Crear directorio de salida si no existe
        os.makedirs(os.path.dirname(audio_salida_wav), exist_ok=True)

        # Verificar formato del archivo de entrada y convertir si es necesario
        if audio_entrada.endswith(".mp3"):
            ruta_temporal = audio_entrada.replace(".mp3", ".wav")
            procesAudio.convertir_mp3_a_wav(audio_entrada, ruta_temporal)
            audio_entrada = ruta_temporal

        # Leer archivo de audio
        datos_audio, tasa_muestreo = procesAudio.leer_audio(audio_entrada)

        # Validar datos de audio
        if len(datos_audio) == 0:
            raise ValueError("El archivo de audio está vacío o corrupto.")

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

        # Guardar la señal reconstruida en WAV
        procesAudio.escribir_audio(audio_salida_wav, señal_reconstruida, tasa_muestreo)
        print(f"Archivo de audio filtrado guardado en: {audio_salida_wav}")

        # Convertir WAV a MP3
        audio = AudioSegment.from_wav(audio_salida_wav)
        audio.export(audio_salida_mp3, format="mp3")
        print(f"Archivo de audio MP3 guardado en: {audio_salida_mp3}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error en los datos o procesamiento: {e}")
    except IOError as e:
        print(f"Error de entrada/salida: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == '__main__':
    main()
