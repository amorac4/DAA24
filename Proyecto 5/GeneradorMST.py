import os
from Sgrafo4 import Grafo

class GeneradorMST:
    def __init__(self, carpeta_entrada, carpeta_salida):
      
        self.carpeta_entrada = carpeta_entrada
        self.carpeta_salida = carpeta_salida

        # Crear la carpeta de salida si no existe
        if not os.path.exists(self.carpeta_salida):
            os.makedirs(self.carpeta_salida)

    def procesar_archivo(self, archivo):
       
        try:
            # Cargar el grafo
            grafo = Grafo.cargarG(archivo)
            print(f"Procesando grafo desde: {archivo}")

            # Generar y guardar MST con Prim
            mst_prim = grafo.prim()
            salida_prim = os.path.join(self.carpeta_salida, f"{os.path.splitext(os.path.basename(archivo))[0]}_prim.gv")
            grafo.guardar_graphviz_algoritmo(salida_prim, mst_prim, "prim")

            # Generar y guardar MST con Kruskal Directo
            mst_kruskal_directo = grafo.kruskalD()
            salida_kruskal_directo = os.path.join(self.carpeta_salida, f"{os.path.splitext(os.path.basename(archivo))[0]}_kruskal_directo.gv")
            grafo.guardar_graphviz_algoritmo(salida_kruskal_directo, mst_kruskal_directo, "kruskal_directo")

            # Generar y guardar MST con Kruskal Inverso
            mst_kruskal_inverso = grafo.kruskalI()
            salida_kruskal_inverso = os.path.join(self.carpeta_salida, f"{os.path.splitext(os.path.basename(archivo))[0]}_kruskal_inverso.gv")
            grafo.guardar_graphviz_algoritmo(salida_kruskal_inverso, mst_kruskal_inverso, "kruskal_inverso")

            print(f"Resultados guardados en: {self.carpeta_salida}")

        except Exception as e:
            print(f"Error procesando el archivo {archivo}: {e}")

    def procesar_carpeta(self):
       
        archivos_grafos = [os.path.join(self.carpeta_entrada, f) for f in os.listdir(self.carpeta_entrada) if f.endswith('.gv')]

        if not archivos_grafos:
            print(f"No se encontraron archivos .gv en la carpeta {self.carpeta_entrada}.")
            return

        for archivo in archivos_grafos:
            print(f"\nProcesando archivo: {archivo}")
            self.procesar_archivo(archivo)

# Ejemplo de uso:
if __name__ == "__main__":
    carpeta_entrada = "/home/verzzul/Escritorio/DAA24/Proyecto 4/Grafos Generados/"
    carpeta_salida = "/home/verzzul/Escritorio/DAA24/Proyecto 4/Grafos MST/"

    generador = GeneradorMST(carpeta_entrada, carpeta_salida)
    generador.procesar_carpeta()