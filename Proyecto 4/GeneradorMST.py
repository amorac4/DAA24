import os
from Kruskal_d4 import Kruskal_D
from Kruskal_i4 import Kruskal_I
from Prim import Prim
from Sgrafo4 import Grafo


def procesar_grafo(archivo, carpeta_salida, nodo_inicial=None):
    try:
        # Cargar el grafo
        grafo = Grafo.cargarG(archivo)
        print(f"\nGrafo cargado desde: {archivo}")

        # Crear la carpeta de salida si no existe
        if not os.path.exists(carpeta_salida):
            os.makedirs(carpeta_salida)

        # Selección del nodo inicial para Prim
        nodo_inicial = nodo_inicial or grafo.nodos[0].id
        nodo_inicial_obj = next((n for n in grafo.nodos if n.id == nodo_inicial), None)
        if not nodo_inicial_obj:
            raise ValueError(f"El nodo inicial '{nodo_inicial}' no se encuentra en el grafo.")

        # Nombre base del grafo
        nombre_base = os.path.splitext(os.path.basename(archivo))[0]

        # Kruskal Directo
        print("Ejecutando Kruskal Directo...")
        kruskal_d = Kruskal_D(grafo)
        mst_kruskal = kruskal_d.gen_mst()
        archivo_salida_kruskal = os.path.join(carpeta_salida, f"{nombre_base}_kruskal.gv")
        mst_kruskal.guardar_graphviz(archivo_salida_kruskal)
        print(f"Kruskal Directo guardado en {archivo_salida_kruskal}")

        # Kruskal Inverso
        print("Ejecutando Kruskal Inverso...")
        kruskal_i = Kruskal_I(grafo)
        mst_kruskal_inverso = kruskal_i.generar_mst()
        archivo_salida_kruskal_inverso = os.path.join(carpeta_salida, f"{nombre_base}_kruskal_inverso.gv")
        mst_kruskal_inverso.guardar_graphviz(archivo_salida_kruskal_inverso)
        print(f"Kruskal Inverso guardado en {archivo_salida_kruskal_inverso}")

        # Prim
        print("Ejecutando Prim...")
        prim = Prim(grafo)
        mst_prim = prim.generar_mst(nodo_inicial_obj)
        archivo_salida_prim = os.path.join(carpeta_salida, f"{nombre_base}_prim.gv")
        mst_prim.guardar_graphviz(archivo_salida_prim)
        print(f"Prim guardado en {archivo_salida_prim}")

    except Exception as e:
        print(f"Error procesando el archivo {archivo}: {e}")


def iniciar_generacion_msts(carpeta_grafos, carpeta_salida, nodo_inicial=None):
    # Validar carpetas
    if not os.path.exists(carpeta_grafos):
        print(f"La carpeta {carpeta_grafos} no existe.")
        return

    if not os.path.exists(carpeta_salida):
        os.makedirs(carpeta_salida)

    # Procesar cada archivo .gv
    archivos_gv = [os.path.join(carpeta_grafos, f) for f in os.listdir(carpeta_grafos) if f.endswith('.gv')]
    if not archivos_gv:
        print(f"No se encontraron archivos .gv en la carpeta {carpeta_grafos}.")
        return

    for archivo in archivos_gv:
        procesar_grafo(archivo, carpeta_salida, nodo_inicial)


if __name__ == "__main__":
    CARPETA_GRAFOS = "/home/verzzul/Escritorio/DAA24/Proyecto 4/Grafos Generados/"
    CARPETA_SALIDA = "/home/verzzul/Escritorio/DAA24/Proyecto 4/Grafos MST/"
    NODO_INICIAL = None  

    iniciar_generacion_msts(CARPETA_GRAFOS, CARPETA_SALIDA, NODO_INICIAL)
