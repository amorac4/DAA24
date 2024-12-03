import copy
from Sgrafo4 import Grafo
from Sarista4 import Arista

class Kruskal_I:
    def __init__(self, grafo):
        self.grafo = grafo

    def generar_mst(self):
        grafo_copia = copy.deepcopy(self.grafo)
        aem = []
        peso_total = 0

        aristas_ordenadas = sorted(self.grafo.aristas, key=lambda arista: arista.peso, reverse=True)

        for arista in aristas_ordenadas:
            grafo_copia.aristas = [a for a in grafo_copia.aristas if a != arista]

            nodos_alcanzados = grafo_copia.bfs(grafo_copia.nodos[0])

            if len(nodos_alcanzados) == len(self.grafo.nodos):
                continue
            else:
                aem.append(arista)
                peso_total += arista.peso
                grafo_copia.agregar_arista(arista)

        print(f"Valor del árbol de expansión mínima por Kruskal Inverso: {round(peso_total, 2)}")
        return aem
