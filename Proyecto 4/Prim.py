import heapq
import random
from Sgrafo4 import Grafo
from Sarista4 import Arista

class Prim:
    def __init__(self, grafo):
        self.grafo = grafo

    def generar_mst(self):
        nodo_inicio = random.choice(list(self.grafo.nodos))

        visitados = set()
        aem = []
        cola_prioridad = []
        peso_total = 0

        for vecino, peso in self.grafo.vecinos_con_peso(nodo_inicio):
            heapq.heappush(cola_prioridad, (peso, nodo_inicio, vecino))

        visitados.add(nodo_inicio)

        while cola_prioridad:
            peso, origen, destino = heapq.heappop(cola_prioridad)

            if destino in visitados:
                continue

            aem.append((origen, destino, peso))
            peso_total += peso
            visitados.add(destino)

            for vecino, peso in self.grafo.vecinos_con_peso(destino):
                if vecino not in visitados:
                    heapq.heappush(cola_prioridad, (peso, destino, vecino))

        print(f"Valor del árbol de expansión mínima por Prim: {round(peso_total, 2)}")
        return aem
