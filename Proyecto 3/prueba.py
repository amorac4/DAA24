from Sgrafo3 import Grafo

# Crear una instancia de Grafo
grafo = Grafo()

# Verificar si el método dijkstra existe
if hasattr(grafo, 'dijkstra'):
    print("El método dijkstra está disponible en la clase Grafo.")
else:
    print("Error: El método dijkstra no se encuentra en la clase Grafo.")
