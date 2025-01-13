import numpy as np
class Filtro:
    # Filtro pasabajas revisado
    def filtro_pasabajas(frecuencias, frecuencia_corte, tasa_muestreo):
        n = len(frecuencias)
        filtrado = np.zeros_like(frecuencias, dtype=complex)  # Garantiza tipo homogéneo
        for k in range(n):
            frecuencia = k * tasa_muestreo / n
            if frecuencia <= frecuencia_corte:
                filtrado[k] = frecuencias[k]
        return filtrado
