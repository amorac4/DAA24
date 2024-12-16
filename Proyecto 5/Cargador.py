import networkx as nx

def cargarG(file_path):
    file_path = "/home/verzzul/Escritorio/DAA24/Proyecto 5/Grafos/grafo_malla_100.gv"
    grafo = nx.read_graphviz(file_path)
    
    return nx.Grafo(grafo)