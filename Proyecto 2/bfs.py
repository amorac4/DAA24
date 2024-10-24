from collections import deque



class BFS:

    def __init__ (self, graph):
        self.graph = graph

    def buscar(self, nodo_inicio):
        #iniciar una cola para BFS
        cola = deque([nodo_inicio])
        #iniciar un conjunto para almacenar los nosos visitados
        visitados = set([nodo_inicio])


        while cola:
            nodo_actual = cola.popleft()
            print(f"Visitado: {nodo_actual.id}")

            for arista in nodo_actual.aristas:
                vecino = arista.n2 if arista.n2 == nodo_actual else arista.n1
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return visitados


