from collections import deque
from Sgrafo import Grafo



class BFS:

    def __init__ (self, graph):
        self.graph = graph

    def buscar(self, nodo_inicio ):
        arbol= Grafo(dirigido=self.dirigido)
        if nodo_inicio not in self.nodos:
          raise ValueError("El nodo de inicio no existe")
        #iniciar una cola para BFS
        cola = deque([nodo_inicio])
        #iniciar un conjunto para almacenar los nosos visitados
        visitados = set([nodo_inicio])
        arbol.agregar_nodo[nodo_inicio]


        while cola:
            nodo_actual = cola.popleft()
            print(f"Visitado: {nodo_actual.id}")

            for vecino in self.vecinos(nodo_actual):
                if vecino.id not in visitados:
                    visitados.add(vecino.id)
                    cola.append(vecino.id)
                    arbol.agregar_nodo(vecino.id)
                    arbol.agregar_aristaA(nodo_actual, vecino.id)
        return arbol


