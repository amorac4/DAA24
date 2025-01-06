import networkx as nx

def cargarG(carpeta):
    try:
        grafo = nx.nx_agraph.read_dot(carpeta)  # Carga el archivo .gv
        return nx.Graph(grafo)  # Convierte a grafo no dirigido
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None