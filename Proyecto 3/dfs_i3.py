# dfs_i.py
from Sarista3 import Arista
from Sgrafo3 import Grafo

class DFS_ITERATIVO:
    def __init__(self, graph):
        self.graph = graph
        self.dirigido = graph.dirigido

    def buscar(self, nodo_inicio):
        arbol = Grafo(dirigido=self.dirigido)
        visitados = set()
        pila = [nodo_inicio]

        arbol.agregar_nodo(nodo_inicio)
        visitados.add(nodo_inicio.id)

        while pila:
            nodo_actual = pila.pop()
            for vecino in self.graph.vecinos(nodo_actual):
                if vecino.id not in visitados:
                    visitados.add(vecino.id)
                    arbol.agregar_nodo(vecino)
                    arbol.agregar_arista(Arista(nodo_actual, vecino))
                    pila.append(vecino)

        return arbol
