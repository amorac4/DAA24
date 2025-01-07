import math

class Spring:
    def __init__(self, grafo, posiciones, ancho, alto, repulsion=500, atraccion=0.01, amortiguacion=0.9, radio=10):
        """
        Inicializa el algoritmo Spring con valores balanceados.
        """
        self.grafo = grafo
        self.posiciones = posiciones
        self.ancho = ancho
        self.alto = alto
        self.repulsion = repulsion
        self.atraccion = atraccion
        self.amortiguacion = amortiguacion
        self.radio = radio  # Nuevo parámetro para limitar posiciones a la pantalla

    def fuerzaDeAtraccion(self, distancia):
        """ Fuerza de atracción lineal entre nodos conectados. """
        return self.atraccion * distancia

    def fuerzaDeRepulsion(self, distancia):
        """ Fuerza de repulsión inversamente proporcional a la distancia. """
        return self.repulsion / (distancia + 1e-9)

    def run(self, iteraciones=1):
        """
        Ejecuta el algoritmo Spring durante un número de iteraciones.
        """
        for _ in range(iteraciones):
            disp = {nodo: [0, 0] for nodo in self.grafo.nodes}

            # Fuerzas de repulsión entre todos los nodos
            for n2 in self.grafo.nodes:
                for n1 in self.grafo.nodes:
                    if n1 != n2:
                        dx = self.posiciones[n2][0] - self.posiciones[n1][0]
                        dy = self.posiciones[n2][1] - self.posiciones[n1][1]
                        dist = math.sqrt(dx**2 + dy**2)
                        fuerza = self.fuerzaDeRepulsion(dist)
                        disp[n2][0] += (dx / (dist + 1e-9)) * fuerza
                        disp[n2][1] += (dy / (dist + 1e-9)) * fuerza

            # Fuerzas de atracción entre nodos conectados
            for n2 in self.grafo.nodes:
                for n1 in self.grafo.neighbors(n2):
                    dx = self.posiciones[n2][0] - self.posiciones[n1][0]
                    dy = self.posiciones[n2][1] - self.posiciones[n1][1]
                    dist = math.sqrt(dx**2 + dy**2)
                    fuerza = self.fuerzaDeAtraccion(dist)
                    disp[n2][0] -= (dx / (dist + 1e-9)) * fuerza
                    disp[n2][1] -= (dy / (dist + 1e-9)) * fuerza

            # Actualizar posiciones y mantenerlas dentro de los límites de la ventana
            for n2 in self.grafo.nodes:
                dx = disp[n2][0] * self.amortiguacion
                dy = disp[n2][1] * self.amortiguacion
                nueva_x = self.posiciones[n2][0] + dx
                nueva_y = self.posiciones[n2][1] + dy

                # Limitar posiciones a los límites de la ventana
                self.posiciones[n2] = (
                    max(self.radio, min(self.ancho - self.radio, nueva_x)),
                    max(self.radio, min(self.alto - self.radio, nueva_y)),
                )
