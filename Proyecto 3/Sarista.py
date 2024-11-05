
# Clase Arista para representar las aristas del grafo.
class Arista:
    def __init__(self, n1, n2, peso):
        self.n1 = n1 # Nodo 1 conectado por la arista
        self.n2 = n2 #Nodo 2 conectado por la arista
        self.peso = peso
        self.atributos = []  # Lista de atributos de la arista

    def __eq__(self, other):
        #Compara dos aristas para verificar si son iguales
        return (self.n1.id == other.n1.id and self.n2.id == other.n2.id) or \
               (self.n1.id == other.n2.id and self.n2.id == other.n1.id)

    def __hash__(self):
        # Devuelve un hash basado en los IDs de los nodos
        return hash((min(self.n1.id, self.n2.id), max(self.n1.id, self.n2.id)))
