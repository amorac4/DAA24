import math
import time

class FruchtermanReingold:

    def __init__(self, grafo, posiciones, ancho, alto, repulsion=500, atraccion=0.01, amortiguacion=0.9):
        self.grafo = grafo
        self.posiciones = posiciones
        self.ancho = ancho
        self.alto = alto
        self.repulsion = repulsion
        self.atraccion = atraccion
        self.amortiguacion = amortiguacion

    def CalRepulsion(self):
        
        desp = {nodo:[0,0]for nodo in self.grafo.nodes}
        for n1 in self.grafo.nodes:
            for n2 in self.grafo.nodes:
                if n1 != n2:
                    dx = self.posiciones[n1][0] - self.posiciones[n2][0]
                    dy = self.posiciones[n1][1] - self.posiciones[n2][1]
                    dist = math.sqrt(dx**2 + dy**2) + 1e-9
                    fuerza = self.repulsion/dist**2

                    desp[n1][0] += (dx / dist)* fuerza
                    desp[n1][1] += (dy / dist)* fuerza
        return desp
    
    def CalAtraccion(self, desp):
        for arista in self.grafo.edges:
            n1, n2 = arista
            dx = self.posiciones[n1][0] - self.posiciones[n2][0]
            dy = self.posiciones[n1][1] - self.posiciones[n2][1]
            dist = math.sqrt(dx**2 + dy**2) + 1e-9
            fuerza = self.atraccion * dist

            desplazamiento = (dx / dist) * fuerza, (dy / dist) * fuerza

            desp[n1][0] -= desplazamiento[0]
            desp[n1][1] -= desplazamiento[1]
            desp[n2][0] += desplazamiento[0]
            desp[n2][1] += desplazamiento[1]
        return desp
    
    def ActuPos (self, desp):
        for nodo in self.grafo.nodes:
            dx, dy =desp[nodo]
            dx *= self.amortiguacion
            dy *= self.amortiguacion

            x = self.posiciones[nodo][0] + dx
            y = self.posiciones[nodo][1] + dy

            self.posiciones[nodo]= (
                max(0, min(self.ancho, x)),
                max(0, min(self.alto, y))
            )
    
    def run(self, iteraciones=1):
        for _ in range(iteraciones):
                desp = self.CalRepulsion()
                desp = self.CalAtraccion(desp)
                self.ActuPos(desp)



