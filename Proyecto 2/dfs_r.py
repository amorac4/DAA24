from Sgrafo import Grafo

class DFS_Recursivo:

    def __init__ (self, graph):
        self.graph = graph


    def buscar (self, nodo_inicio):
        arbol = Grafo(dirigido=self.dirigido)
        if nodo_inicio not in self.nodos:
            raise ValueError("El nodo de inicio no exite")
        visitados = set()
        arbol.agregar_nodo(nodo_inicio)

        
    
        def DFS_R_Auxiliar (nodo):
       
          visitados.add(nodo)
          for vecino in self.vecinos(nodo):
              if vecino.id not in visitados:
                  visitados.add(vecino.id)
                  arbol.agregar_nodo(vecino.id)
                  arbol.agregar_aristaA(nodo, vecino.id)
                  DFS_R_Auxiliar(vecino.id)
        
        DFS_R_Auxiliar(nodo_inicio)
              
        return arbol 