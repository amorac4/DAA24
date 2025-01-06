class QuadtreeNode:
    def __init__(self, x_min, x_max, y_min, y_max):
       
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.hijos = []  # Subdivisiones del nodo
        self.objetos = []  # Nodos almacenados en este espacio
        self.centro_masa = None
        self.total_masa = 0

    def insertar(self, objeto, x, y):
        
        if len(self.hijos) == 0:
            self.objetos.append((objeto, x, y))

            if len(self.objetos) > 1 and (self.x_max - self.x_min > 1 or self.y_max - self.y_min > 1):
                self._subdividir()
        else:
            for hijo in self.hijos:
                if hijo.contiene(x, y):
                    hijo.insertar(objeto, x, y)

    def contiene(self, x, y):
        
        return self.x_min <= x < self.x_max and self.y_min <= y < self.y_max

    def _subdividir(self):
        """
        Subdivide el nodo en cuatro hijos y distribuye los objetos existentes.
        """
        x_medio = (self.x_min + self.x_max) / 2
        y_medio = (self.y_min + self.y_max) / 2

        self.hijos = [
            QuadtreeNode(self.x_min, x_medio, self.y_min, y_medio),
            QuadtreeNode(x_medio, self.x_max, self.y_min, y_medio),
            QuadtreeNode(self.x_min, x_medio, y_medio, self.y_max),
            QuadtreeNode(x_medio, self.x_max, y_medio, self.y_max)
        ]

        for objeto, x, y in self.objetos:
            for hijo in self.hijos:
                if hijo.contiene(x, y):
                    hijo.insertar(objeto, x, y)

        self.objetos = []

    def calcular_centro_masa(self):
        
        if len(self.hijos) == 0:
            if len(self.objetos) == 0:
                self.centro_masa = (0, 0)
                self.total_masa = 0
            else:
                x_total = sum(x for _, x, _ in self.objetos)
                y_total = sum(y for _, _, y in self.objetos)
                self.total_masa = len(self.objetos)
                self.centro_masa = (x_total / self.total_masa, y_total / self.total_masa)
        else:
            x_total = 0
            y_total = 0
            self.total_masa = 0

            for hijo in self.hijos:
                hijo.calcular_centro_masa()
                x_total += hijo.centro_masa[0] * hijo.total_masa
                y_total += hijo.centro_masa[1] * hijo.total_masa
                self.total_masa += hijo.total_masa

            if self.total_masa > 0:
                self.centro_masa = (x_total / self.total_masa, y_total / self.total_masa)
            else:
                self.centro_masa = (0, 0)
