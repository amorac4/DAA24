

class DFS_ITERATIVO:

    def __init__(self, graph):
        self.graph

    def buscar (self, nodo_inicio):

        pila = [nodo_inicio]
        visitados = set()
        orden =[]

        while pila:
            nodo_actual = pila.pop()

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                orden.append(nodo_actual)
                print(f"Visitado: {nodo_actual.id}")

                for arista in reversed(nodo_actual.aristas):
                    vecino = arista.n2 if arista.n1 == nodo_actual else arista.n1
                    if vecino not in visitados:
                        pila.append(vecino)
            return orden