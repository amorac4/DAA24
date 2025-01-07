import math
from QuadtreeNode import QuadtreeNode

class BarnesHut:
    def __init__(self, x_min, x_max, y_min, y_max, theta=0.5):
        self.theta = theta
        self.quadtree = QuadtreeNode(x_min, x_max, y_min, y_max)
        self.posiciones = {}  # Inicializa el diccionario de posiciones

    def construirQ(self, objetos):
        for objeto, x, y in objetos:
            self.quadtree.insertar(objeto, x, y)
        self.quadtree.calcular_centro_masa()

    def CalFuerza(self, objetivo, x, y):
        def FuerzaRecursiva(nodo, x, y):
            if len(nodo.hijos) == 0:
                fuerza_x, fuerza_y = 0, 0
                for objeto, obj_x, obj_y in nodo.objetos:
                    if objeto != objetivo:
                        dx = obj_x - x
                        dy = obj_y - y
                        dist = math.sqrt(dx**2 + dy**2) + 1e-9
                        fuerza = 1 / dist**2  # Simplificación de fuerza de repulsión
                        fuerza_x += (dx / dist) * fuerza
                        fuerza_y += (dy / dist) * fuerza
                return fuerza_x, fuerza_y
            else:
                dx = nodo.centro_masa[0] - x
                dy = nodo.centro_masa[1] - y
                dist = math.sqrt(dx**2 + dy**2) + 1e-9
                s = nodo.x_max - nodo.x_min
                if s / dist < self.theta:
                    fuerza = nodo.total_masa / dist**2
                    fuerza_x = (dx / dist) * fuerza
                    fuerza_y = (dy / dist) * fuerza
                    return fuerza_x, fuerza_y
                else:
                    total_fx, total_fy = 0, 0
                    for hijo in nodo.hijos:
                        if hijo is not None:
                            fx, fy = FuerzaRecursiva(hijo, x, y)
                            total_fx += fx
                            total_fy += fy
                    return total_fx, total_fy
            return 0, 0
        return FuerzaRecursiva(self.quadtree, x, y)

    def ActuPos(self, nodos, posiciones, fuerza_factor=0.01):
        nuevas_posiciones = {}
        for nodo in nodos:
            x, y = posiciones[nodo]
            fx, fy = self.CalFuerza(nodo, x, y)
            nx = x + fuerza_factor * fx
            ny = y + fuerza_factor * fy
            nuevas_posiciones[nodo] = (nx, ny)
        self.posiciones = nuevas_posiciones  # Actualiza el atributo `posiciones`
        return self.posiciones

