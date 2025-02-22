# bfs.py
from collections import deque
from Sarista import Arista
from Sgrafo import Grafo

class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.dirigido = graph.dirigido

    def buscar(self, nodo_inicio):
        arbol = Grafo(dirigido=self.dirigido)
        visitados = set()
        cola = deque([nodo_inicio])

        arbol.agregar_nodo(nodo_inicio)
        visitados.add(nodo_inicio.id)

        while cola:
            nodo_actual = cola.popleft()
            for vecino in self.graph.vecinos(nodo_actual):
                if vecino.id not in visitados:
                    visitados.add(vecino.id)
                    arbol.agregar_nodo(vecino)
                    arbol.agregar_arista(Arista(nodo_actual, vecino))
                    cola.append(vecino)

        return arbol
