import cmath

class FFT:
#fft
    def fft (n, a):
        
        if n == 1:
            return a
        pares   = FFT.fft(n // 2, a[0::2])
        impares = FFT.fft(n // 2, a[1::2])
        resultado = [0] * n

        for k in range(n // 2):
            omega_k = cmath.exp(-2j * cmath.pi * k / n)
            resultado[k] = pares[k] + omega_k * impares[k]
            resultado[k + n // 2] = pares[k] - omega_k * impares [k]

        return resultado
    

