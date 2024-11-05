# Snodo3.py

# Clase Nodo que representa un nodo en el grafo
class Nodo:
    def __init__(self, id):
        self.id = id  # Identificador único del nodo
        self.aristas = set()  # Conjunto de aristas conectadas al nodo
        self.atributos = []  # Lista de atributos

    def __repr__(self):
        # Representación del nodo, muestra ID y la cantidad de aristas
        return f"Nodo(id={self.id}, aristas={len(self.aristas)}, atributos={self.atributos})"

    def __lt__(self, otro):
        # Método para comparar nodos basado en su ID, necesario para usar heapq
        return self.id < otro.id
