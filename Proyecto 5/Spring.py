import math

class Spring:
    
    def __init__(self, grafo, posiciones, ancho, alto, repulsion=2, atraccion=1):

        self.grafo = grafo
        self.posiciones = posiciones
        self.ancho = ancho
        self,alto = alto
        self.repulsion = repulsion
        self.atraccion = repulsion

    def fuerzaDeAtraccion (self, distancia):
        return self.atraccion * math.log(distancia/self.atraccion) if distancia > 0 else 0
    
    def fuerzaDeRepulsion (self, distancia):
        return self.repulsion / math.sqrt(distancia) if distancia > 0 else 0
    
    def run(self, iteracines=100):
        disp= {nodo: [0, 0] for nodo in self.grafo.nodos}

        for _ in range(iteracines):

            for n2 in self.grafo.nodos:
                disp[n2] = [0,0]
                for n1 in self.grafo.nodos:
                    if n2 != n1:
                        dx= self.posiciones[n2][0] - self.posiciones[n1][0]
                        dy= self.posiciones[n2][1] - self.posiciones[n1][1]
                        dist = math.sqrt(dx**2 + dy**2)
                        fuerza = self.fuerzaDeRepulsion(dist)
                        disp[n2][0] += (dx / dist) * fuerza if dist > 0 else 0
                        disp[n2][1] += (dy / dist) * fuerza if dist > 0 else 0

            for n2 in self.grafo.nodos:
                self.posiciones[n2]=(
                    max(0, min(self.ancho, self.posiciones[n2][0] + disp[n2][0])),
                    max(0, min(self.alto, self.posiciones[n2][1] + disp[n2][1])),
                )



    