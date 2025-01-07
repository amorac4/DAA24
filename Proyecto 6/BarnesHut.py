import math
from QuadtreeNode import QuadtreeNode

class BarnesHut:
    def __init__(self, x_min, x_max, y_min, y_max, theta=0.5, repulsion=250, atraccion=0.01, min_distancia=5):
        self.theta = theta
        self.repulsion = repulsion
        self.atraccion = atraccion
        self.min_distancia = min_distancia
        self.quadtree = QuadtreeNode(x_min, x_max, y_min, y_max)
        self.posiciones = {}  # Diccionario para almacenar las posiciones de los nodos

    def construirQ(self, nodos):
        self.quadtree = QuadtreeNode(0, 1200, 0, 700)  # Redimensiona para el espacio de trabajo
        for nodo_id, (x, y) in nodos.items():
            self.quadtree.insertar(nodo_id, x, y)  # Desglosa la tupla (x, y) correctamente
        self.quadtree.calcular_centro_masa()

    def calcular_fuerzas_atractivas(self, grafo, posiciones):
        fuerzas = {nodo: [0, 0] for nodo in grafo.nodes}

        for nodo1, nodo2 in grafo.edges:
            x1, y1 = posiciones[nodo1]
            x2, y2 = posiciones[nodo2]
            dx, dy = x2 - x1, y2 - y1
            dist = math.sqrt(dx**2 + dy**2) + 1e-9
            fuerza = self.repulsion * math.log(dist + 1)  # Puedes ajustar esta fórmula según sea necesario

    def calcular_fuerzas_atractivas(self, grafo, posiciones):
      
        if grafo is None:
            raise ValueError("El grafo no puede ser None.")

        fuerzas = {nodo: [0, 0] for nodo in grafo.nodes}

        for nodo1, nodo2 in grafo.edges:
            x1, y1 = posiciones[nodo1]
            x2, y2 = posiciones[nodo2]
            dx, dy = x2 - x1, y2 - y1
            dist = math.sqrt(dx**2 + dy**2) + 1e-9

            fuerza = self.atraccion * dist

            fuerzas[nodo1][0] += fuerza * dx / dist
            fuerzas[nodo1][1] += fuerza * dy / dist
            fuerzas[nodo2][0] -= fuerza * dx / dist
            fuerzas[nodo2][1] -= fuerza * dy / dist

        return fuerzas



    def calcular_fuerzas_repulsivas(self, nodo_id, nodo_pos):
        
        fuerza = [0, 0]

        def fuerza_recursiva(nodo, pos, fuerza):
            if nodo.total_masa == 0 or nodo.centro_masa is None:
                return

            dx = nodo.centro_masa[0] - pos[0]
            dy = nodo.centro_masa[1] - pos[1]
            dist = math.sqrt(dx**2 + dy**2) + 1e-9

            if dist < self.min_distancia:
                return

            if (nodo.x_max - nodo.x_min) / dist < self.theta or len(nodo.hijos) == 0:
                fuerza_repulsiva = self.repulsion * nodo.total_masa / (dist**2)
                fuerza[0] -= fuerza_repulsiva * dx / dist
                fuerza[1] -= fuerza_repulsiva * dy / dist
            else:
                for hijo in nodo.hijos:
                    if hijo is not None:
                        fuerza_recursiva(hijo, pos, fuerza)

        fuerza_recursiva(self.quadtree, nodo_pos, fuerza)
        return tuple(fuerza)

    def ActuPos(self, grafo, posiciones, fuerza_factor=0.05):
        """
        Actualiza las posiciones de los nodos combinando fuerzas repulsivas y atractivas.
        :param grafo: Grafo con las conexiones entre nodos.
        :param posiciones: Diccionario {nodo_id: (x, y)} con las posiciones actuales.
        :param fuerza_factor: Escala de las fuerzas para ajustar la magnitud del desplazamiento.
        :return: Diccionario actualizado con las nuevas posiciones.
        """
        nuevas_posiciones = {}
        self.construirQ(posiciones)  # Construye el Quadtree basado en posiciones

        nodos = list(grafo.nodes)  # Obtener nodos del grafo
        # Calcula fuerzas repulsivas para cada nodo
        fuerzas_repulsivas = {nodo: self.calcular_fuerzas_repulsivas(nodo, posiciones[nodo]) for nodo in nodos}
        # Calcula fuerzas atractivas entre nodos conectados
        fuerzas_atractivas = self.calcular_fuerzas_atractivas(grafo, posiciones)

        # Actualiza las posiciones combinando las fuerzas
        for nodo in nodos:
            x, y = posiciones[nodo]
            fx_rep, fy_rep = fuerzas_repulsivas[nodo]
            fx_att, fy_att = fuerzas_atractivas[nodo]

            # Combina las fuerzas
            fx = fx_rep + fx_att
            fy = fy_rep + fy_att

            # Actualiza la posición
            nuevas_x = max(10, min(1190, x + fuerza_factor * fx))
            nuevas_y = max(10, min(690, y + fuerza_factor * fy))
            nuevas_posiciones[nodo] = (nuevas_x, nuevas_y)

        self.posiciones = nuevas_posiciones
        return nuevas_posiciones
    
    def dibujar_quadtree(self, pantalla):
    
        if self.quadtree:
            self.quadtree.dibujar(pantalla)
