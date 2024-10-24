import sys
import os

proyecto_1_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../proyecto 1'))
if proyecto_1_path not in sys.path:
   sys.path.append(proyecto_1_path)


from bfs import BFS
from dfs_r import DFS_Recursivo
from dfs_i import DFS_ITERATIVO
from Sgrafo import grafoBarabasiAlbert, grafoDorogovtsevMendes, grafoErdosRenyi, grafoGeografico, grafoGilbert, grafoMalla


def generar_grafos():

    nodo_list =[30, 100, 500]
    grafos =[]


    for nodos in nodo_list:

        grafos.append(("Erdös-Rényi",grafoErdosRenyi(nodos, int(nodos*1.5))))
        grafos.append(("Gilbert", grafoGilbert(nodos, 0.1)))
        grafos.append(("Geografico", grafoGeografico(nodos, 0.2)))
        grafos.append(("Barabási-Albert",grafoBarabasiAlbert(nodos, 4)))
        grafos.append(("Dorogovtsev-Mendes", grafoDorogovtsevMendes(nodos)))

    return grafos


def iniciar_busqueda():
    grafos = generar_grafos()


    malla =[

        ("Malla", grafoMalla(5,6)),
        ("Malla", grafoMalla(10,10)),
        ("Malla", grafoMalla(25,20)),
    ]

    grafos.extend(malla)


    for nombre, grafo in grafos:
        print(f"\nGrafo generado: {nombre} con {len(grafo.nodos)} nodos")
        grafo.mostrat_grafo()

        nodo_inicio = grafo.nodos[0] if grafo.nodos else None
        if not nodo_inicio:
            print(f"No hay nodos en el grafo {nombre}.")
            continue

        print("\nBusqueda en amplitud(BFS):")
        bfs = BFS(grafo)
        bfs.buscar(nodo_inicio)

        print("\nBusqueda en profundidad Recursiva (DFS RECURSIVO):")
        dfsR = DFS_Recursivo(grafo)
        dfsR.buscar(nodo_inicio)

        print("\nBusqueda en profundidad iterativa(BFS ITERATIVO):")
        dfsI = DFS_ITERATIVO(grafo)
        dfsI.buscar(nodo_inicio)

        if __name__ == "__main__":
            iniciar_busqueda()