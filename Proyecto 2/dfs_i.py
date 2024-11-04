from Sgrafo import Grafo

class DFS_ITERATIVO:

    def __init__(self, graph):
        self.graph

    def buscar (self, nodo_inicio):
        arbol= Grafo(dirigido=self.dirigido)
        if nodo_inicio not in self.nodos:
          raise ValueError("El nodo de inicio no existe")
        pila = [nodo_inicio]
        visitados = {nodo_inicio}
        arbol.agregar_nodo(nodo_inicio)

        while pila:
            nodo_actual = pila.pop()
            for vecino in self.vecinos(nodo_actual):
                visitados.add(vecino.id)
                pila.append(vecino.id)
                arbol.agregar_nodo(vecino.id)
                arbol.agregar_aristaA(nodo_actual, vecino.id)
            return arbol