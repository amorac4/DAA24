
from bfs import BFS
from dfs_r import DFS_Recursivo
from dfs_i import DFS_ITERATIVO
from Generador import GenGrafo
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







