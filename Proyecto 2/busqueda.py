import sys
sys.path.append("/home/verzzul/Escritorio/DAA24/Proyecto 1")

from bfs import BFS
from dfs_r import DFS_Recursivo
from dfs_i import DFS_ITERATIVO
from Sgrafo import  grafoBarabasiAlbert, grafoDorogovtsevMendes, grafoErdosRenyi, grafoGeografico, grafoGilbert, grafoMalla

def resultados_busqueda(nombre, tipo_busqueda, nodos_visitados):
    filename = f"Resultado de {tipo_busqueda}en el grafo: {nombre}.txt"
    with open(filename, 'w') as f:
        f.write(f"Resultado de {tipo_busqueda} en el grafo: {nombre}\n")
        f.write("Nodos visitados en orden:\n")
        for nodo in nodos_visitados:
            f.write(f" {nodo.id}\n")

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
        
        grafo.mostrar_grafo()

        grafo.guardar_graphviz(f"{nombre}_generado.gv")

        nodo_inicio = grafo.nodos[0] if grafo.nodos else None
        if not nodo_inicio:
            print(f"No hay nodos en el grafo {nombre}.")
            continue

        print("\nBusqueda en amplitud(BFS):")
        bfs = BFS(grafo)
        bfs.buscar(nodo_inicio)
        resultados_busqueda(nombre, "BFS", bfs.visitados)

        print("\nBusqueda en profundidad Recursiva (DFS RECURSIVO):")
        dfsR = DFS_Recursivo(grafo)
        dfsR.buscar(nodo_inicio)
        resultados_busqueda(nombre, "DFS_R", dfsR.visitados)

        print("\nBusqueda en profundidad iterativa(DFS ITERATIVO):")
        dfsI = DFS_ITERATIVO(grafo)
        dfsI.buscar(nodo_inicio)
        resultados_busqueda(nombre, "DFS_I", dfsI.vsitados)

if __name__ == "__main__":
            iniciar_busqueda()