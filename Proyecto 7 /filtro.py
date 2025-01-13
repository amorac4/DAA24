class Filtro:

#Filtro pasabajas
    def filtro_pasabajas(frecuencias, frecuencia_corte, tasa_muestreo):
        filtrado = []
        n =len(frecuencias)
        for k in range(n):
            frecuencia = k * tasa_muestreo / n
            if frecuencia <= frecuencia_corte:
                filtrado.append(frecuencias[k])
            else:
                filtrado.append(0)
        return filtrado
