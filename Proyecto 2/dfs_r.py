

class DFS_Recursivo:

    def __init__ (self, graph):
        self.graph = graph

    def DFS_R_Auxiliar (self, node, visitados):
        
        visitados.add(node)
        print (f"Visitado: {node.id}")

        for arista in node.aristas:
            vecino = arista.n2 if arista.n1 == node else arista.n1
            if vecino not in visitados:
                self.DFS_R_Auxiliar(vecino, visitados)
    def buscar (self, nodo_inicio):

        visitados = set()
        self.DFS_R_Auxiliar(nodo_inicio, visitados)
        return visitados