# dfs_r.py
from Sarista4 import Arista
from Sgrafo4 import Grafo

class DFS_Recursivo:
    def __init__(self, graph):
        self.graph = graph
        self.dirigido = graph.dirigido

    def buscar(self, nodo_inicio):
        arbol = Grafo(dirigido=self.dirigido)
        visitados = set()

        def DFS_R_Auxiliar(nodo):
            visitados.add(nodo.id)
            arbol.agregar_nodo(nodo)
            for vecino in self.graph.vecinos(nodo):
                if vecino.id not in visitados:
                    arbol.agregar_arista(Arista(nodo, vecino))
                    DFS_R_Auxiliar(vecino)

        DFS_R_Auxiliar(nodo_inicio)
        return arbol
