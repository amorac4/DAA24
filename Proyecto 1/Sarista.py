class Arista:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.atributos = []  # Lista de atributos

    def __eq__(self, other):
        return (self.n1.id == other.n1.id and self.n2.id == other.n2.id) or \
               (self.n1.id == other.n2.id and self.n2.id == other.n1.id)

    def __hash__(self):
        # Devuelve un hash basado en los IDs de los nodos
        return hash((min(self.n1.id, self.n2.id), max(self.n1.id, self.n2.id)))
