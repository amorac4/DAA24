from Sgrafo import grafoMalla, grafoErdosRenyi, grafoGilbert, grafoGeografico, grafoBarabasiAlbert, grafoDorogovtsevMendes

class GenGrafo:
    def __init__(self, nodos):
        self.nodos = nodos

    def crear_y_mostrar_grafo(self, grafo_func, nombre, *args):
        """Crea un grafo usando una función y lo muestra."""
        try:
            grafo = grafo_func(self.nodos, *args)
            print(f"Grafo {nombre}:")
            grafo.mostrar_grafo()
            grafo.guardar_graphviz(f"grafo_{nombre}_{self.nodos}.gv")
        except Exception as e:
            print(f"Error al crear {nombre}: {e}")

    def crear_grafos(self):
        """Crea varios tipos de grafos y los muestra."""
        print(f"\nEjemplo con {self.nodos} nodos:")
        self.crear_y_mostrar_grafo(grafoErdosRenyi, "Erdös-Rényi", int(self.nodos * (self.nodos - 1) / 2 * 0.1))
        self.crear_y_mostrar_grafo(grafoGilbert, "Gilbert", 0.1)
        self.crear_y_mostrar_grafo(grafoGeografico, "Geográfico", 0.1)
        self.crear_y_mostrar_grafo(grafoBarabasiAlbert, "Barabási-Albert", 2)
        self.crear_y_mostrar_grafo(grafoDorogovtsevMendes, "Dorogovtsev-Mendes")

def ejecutar_ejemplos():
    """Crea grafos de malla y ejemplos de otros grafos."""
    nodos_list = [ 30, 100, 500]
    
    # Crear grafos de malla
    for filas, columnas in [(5, 6), (20, 5), (25, 20)]:
        grafo_malla = grafoMalla(filas, columnas)
        print(f"Grafo de Malla ({filas * columnas} nodos):")
        grafo_malla.mostrar_grafo()
        grafo_malla.guardar_graphviz(f"grafo_malla_{filas * columnas}.gv")

    # Crear ejemplos de otros grafos
    for nodos in nodos_list:
        ejemplo = GenGrafo(nodos)
        ejemplo.crear_grafos()

if __name__ == "__main__":
    ejecutar_ejemplos()