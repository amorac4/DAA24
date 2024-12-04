
from Sgrafo4 import Grafo
from Sarista4 import Arista

class Kruskal_D:
    def __init__(self, grafo):
        self.grafo = grafo

    def generar_mst(self):
        # Inicializar conjuntos disjuntos para todos los nodos
        for nodo in self.grafo.nodos:
            self.grafo.conjunto_disjunto(nodo)

        mst = Grafo(dirigido=False)
        for nodo in self.grafo.nodos:
            mst.agregar_nodo(nodo)

        for arista in self.grafo.aristas_ordenadas():
            if self.grafo.find(arista.n1.id) != self.grafo.find(arista.n2.id):
                mst.agregar_arista(arista)
                self.grafo.union(self.grafo.familia, arista.n1.id, arista.n2.id)

        return mst