import os
from Sgrafo import Grafo, cargarG, dijkstra
from Snodo import Nodo

# Ruta a la carpeta donde se encuentran los archivos de grafos en formato .gv
CARPETA_GRAFOS = "/home/verzzul/Escritorio/DAA24/Proyecto 3/ejemplos_grafo_dijkstra/"

def ejecutar_dijkstra_en_grafos():
    if not os.path.exists(CARPETA_GRAFOS):
        print(f"La carpeta {CARPETA_GRAFOS} no existe.")
        return

    # Listar todos los archivos .gv en la carpeta
    archivos_gv = [f for f in os.listdir(CARPETA_GRAFOS) if f.endswith('.gv')]
    if not archivos_gv:
        print(f"No se encontraron archivos .gv en la carpeta {CARPETA_GRAFOS}.")
        return

    # Ejecutar Dijkstra para cada archivo
    for archivo in archivos_gv:
        ruta_archivo = os.path.join(CARPETA_GRAFOS, archivo)
        print(f"Procesando grafo desde: {archivo}")

        # Cargar el grafo
        grafo = cargarG(ruta_archivo)
        if not isinstance(grafo, Grafo):
            print(f"Error: El archivo {archivo} no cargó un objeto de tipo Grafo.")
            continue

        if not grafo.nodos:
            print(f"El grafo en {archivo} no tiene nodos.")
            continue

        # Usar el primer nodo como nodo fuente
        nodo_inicio = grafo.nodos[0]
        print(f"Nodo fuente: {nodo_inicio.id}")

        # Ejecutar el algoritmo de Dijkstra
        distancias = grafo.dijkstra(nodo_inicio)
        print("Distancias desde el nodo fuente:")
        for nodo, distancia in distancias.items():
            print(f"  {nodo.id}: {distancia}")

        # Guardar el resultado en un archivo .gv con prefijo "dijkstra_"
        nombre_salida = os.path.join(CARPETA_GRAFOS, f"dijkstra_{archivo}")
        grafo.guardar_graphviz(nombre_salida)
        print(f"Grafo con distancias guardado en: {nombre_salida}")
        print("\n----------------------------------------\n")

if __name__ == "__main__":
    ejecutar_dijkstra_en_grafos()
