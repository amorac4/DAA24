import cmath


class IFFT:
#fft inverso
    def ifft (n, a):
        
        if n == 1:
            return a
        pares   = IFFT.ifft(n // 2, a[0::2])
        impares = IFFT.ifft(n // 2, a[1::2])
        resultado = [0] * n

        for k in range(n // 2):
            omega_k = cmath.exp(2j * cmath.pi * k / n)
            resultado[k] = (pares[k] + omega_k * impares[k])/n
            resultado[k + n // 2] = (pares[k] - omega_k * impares [k])/n
            
        return resultado
    
