
import os
import random
from bfs import BFS
from dfs_r import DFS_Recursivo
from dfs_i import DFS_ITERATIVO
from Sgrafo import Grafo, cargarG

# Ruta a la carpeta con los archivos .gv
CARPETA_GRAFOS = "/home/verzzul/Escritorio/DAA24/Proyecto 2/ejemplos_grafos_buscados/"

def procesar_grafo(archivo):
    try:
        # Cargar el grafo desde el archivo
        grafo = cargarG(archivo)
        print(f"Grafo cargado desde: {archivo}")

        # Elegir un nodo inicial aleatorio
        nodo_inicial = random.choice(grafo.nodos)
        print("Nodo inicial:", nodo_inicial.id)

        # BFS
        try:
            print("\nEjecutando BFS...")
            bfs = BFS(grafo)
            arbol_bfs = bfs.buscar(nodo_inicial)
            arbol_bfs.guardar_graphviz(f"{archivo[:-3]}_bfs.gv")
            print(f"BFS completado. Nodos visitados: {len(arbol_bfs.nodos)}")
        except Exception as e:
            print(f"Error en BFS: {e}")

        # DFS Recursivo
        try:
            print("\nEjecutando DFS Recursivo...")
            dfs_r = DFS_Recursivo(grafo)
            arbol_dfsr = dfs_r.buscar(nodo_inicial)
            arbol_dfsr.guardar_graphviz(f"{archivo[:-3]}_dfs_r.gv")
            print(f"DFS Recursivo completado. Nodos visitados: {len(arbol_dfsr.nodos)}")
        except Exception as e:
            print(f"Error en DFS Recursivo: {e}")

        # DFS Iterativo
        try:
            print("\nEjecutando DFS Iterativo...")
            dfs_i = DFS_ITERATIVO(grafo)
            arbol_dfsi = dfs_i.buscar(nodo_inicial)
            arbol_dfsi.guardar_graphviz(f"{archivo[:-3]}_dfs_i.gv")
            print(f"DFS Iterativo completado. Nodos visitados: {len(arbol_dfsi.nodos)}")
        except Exception as e:
            print(f"Error en DFS Iterativo: {e}")

    except Exception as e:
        print(f"Error procesando el archivo {archivo}: {e}")

def iniciar_busqueda():
    # Cargar todos los archivos .gv desde la carpeta especificada
    if not os.path.exists(CARPETA_GRAFOS):
        print(f"La carpeta {CARPETA_GRAFOS} no existe.")
        return

    archivos_gv = [os.path.join(CARPETA_GRAFOS, f) for f in os.listdir(CARPETA_GRAFOS) if f.endswith('.gv')]

    if not archivos_gv:
        print(f"No se encontraron archivos .gv en la carpeta {CARPETA_GRAFOS}.")
        return

    for archivo in archivos_gv:
        procesar_grafo(archivo)

if __name__ == "__main__":
    iniciar_busqueda()
