#se importan las funciones del modulo Sgrafo
from Sgrafo3 import grafoMalla, grafoErdosRenyi, grafoGilbert, grafoGeografico, grafoBarabasiAlbert, grafoDorogovtsevMendes

# Clase GenGrafo para manejar la generacion y visualizacion de ls grafos.
class GenGrafo:
    def __init__(self, nodos):
        self.nodos = nodos # numero de nodis a generar

    def crear_y_mostrar_grafo(self, grafo_func, nombre, *args):
        # Crea un grafo usando una función y lo muestra.
        try:
            grafo = grafo_func(self.nodos, *args)
            print(f"Grafo {nombre}:")
            grafo.mostrar_grafo()
            grafo.guardar_graphviz(f"grafo_{nombre}_{self.nodos}.gv")
        #Guarda el grafo en un archivo .gv para Graphviz.
        except Exception as e:
            print(f"Error al crear {nombre}: {e}")

    def crear_grafos(self):
        #Crea varios tipos de grafos y los muestra.
        print(f"\nEjemplo con {self.nodos} nodos:")
        self.crear_y_mostrar_grafo(grafoErdosRenyi, "Erdös-Rényi", int(self.nodos * (self.nodos - 1) / 2 * 0.1))
        self.crear_y_mostrar_grafo(grafoGilbert, "Gilbert", 0.1)
        self.crear_y_mostrar_grafo(grafoGeografico, "Geográfico", 0.3)
        self.crear_y_mostrar_grafo(grafoBarabasiAlbert, "Barabási-Albert", 7)
        self.crear_y_mostrar_grafo(grafoDorogovtsevMendes, "Dorogovtsev-Mendes")

#Funcion principal para ejecutar la generacion de los ejemplos
def ejecutar_ejemplos():
    # lista de tamaños de nodod para los ejemplos
    nodos_list = [ 30, 500]
    
    # Crear grafos de malla
    for filas, columnas in [(5, 6), (25, 20)]:
        grafo_malla = grafoMalla(filas, columnas)
        print(f"Grafo de Malla ({filas * columnas} nodos):")
        grafo_malla.mostrar_grafo()
        grafo_malla.guardar_graphviz(f"grafo_malla_{filas * columnas}.gv")

    # Crear ejemplos de otros grafos
    for nodos in nodos_list:
        ejemplo = GenGrafo(nodos)
        ejemplo.crear_grafos()

if __name__ == "__main__":
    ejecutar_ejemplos() #Ejecuta los ejemplos si el script es ejecutado
