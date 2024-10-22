#clase Nondo que representa un nodo en el grafo
class Nodo:
    def __init__(self, id):
        self.id = id # identificado unico del nodo
        self.aristas = set()#Conjunto de aristas conectadas al nodo
        self.atributos = []  # Lista de atributos

    def __repr__(self):
        #Representacion del nodo, muestra ID y la cantidad de aristas
        return f"Nodo(id={self.id}, aristas={len(self.aristas)}, atributos={self.atributos})"