import random
import math
from Snodo import Nodo
from Sarista import Arista

class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = []
        self.aristas = set()
        self.dirigido = dirigido

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def existe_arista(self, arista):
        """Verifica si la arista ya existe en el grafo."""
        if self.dirigido:
            return arista in self.aristas
        else:
            return arista in self.aristas or Arista(arista.n2, arista.n1) in self.aristas

    def agregar_arista(self, arista):
        """Agrega una arista si no existe ya en el grafo."""
        if not self.existe_arista(arista):
            self.aristas.add(arista)

    def guardar_graphviz(self, filename):
        """Guarda el grafo en formato .dot para usar con Graphviz."""
        with open(filename, 'w') as f:
            f.write("digraph G {\n" if self.dirigido else "graph G {\n")
            for arista in self.aristas:
                if self.dirigido:
                    f.write(f'    "{arista.n1.id}" -> "{arista.n2.id}";\n')
                else:
                    f.write(f'    "{arista.n1.id}" -- "{arista.n2.id}";\n')
            f.write("}\n")

    def mostrar_grafo(self):
        """Imprime la estructura del grafo."""
        print(f"Grafo {'dirigido' if self.dirigido else 'no dirigido'} con {len(self.nodos)} nodos y {len(self.aristas)} aristas.")

def generar_nodos(n, nombre_prefix="n"):
    """Genera n nodos con un prefijo de nombre."""
    return [Nodo(f"{nombre_prefix}{i}") for i in range(n)]

def grafoMalla(m, n, dirigido=False):
    """Genera un grafo de malla de tamaño m x n."""
    if m <= 1 or n <= 1:
        raise ValueError("Los valores de m y n deben ser mayores que 1.")
    
    grafo = Grafo(dirigido)
    nodos = [[Nodo(f"n{i}_{j}") for j in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            # Agregar nodo al grafo
            grafo.agregar_nodo(nodos[i][j])
            
            # Conectar con el nodo de abajo si no está en el borde inferior
            if i < m - 1:
                grafo.agregar_arista(Arista(nodos[i][j], nodos[i + 1][j]))
            
            # Conectar con el nodo a la derecha si no está en el borde derecho
            if j < n - 1:
                grafo.agregar_arista(Arista(nodos[i][j], nodos[i][j + 1]))
    
    return grafo

def grafoErdosRenyi(n, m, dirigido=False):
    """Genera un grafo aleatorio según el modelo Erdös-Rényi."""
    if n <= 0:
        raise ValueError("El número de nodos debe ser mayor que 0.")
    if m < n - 1:
        raise ValueError("El número de aristas debe ser al menos n-1.")
    
    grafo = Grafo(dirigido)
    nodos = [Nodo(i) for i in range(n)]
    
    for nodo in nodos:
        grafo.agregar_nodo(nodo)

    aristas = set()
    while len(aristas) < m:
        n1, n2 = random.sample(range(n), 2)
        if dirigido:
            aristas.add((n1, n2))
        else:
            aristas.add(tuple(sorted([n1, n2])))

    for n1, n2 in aristas:
        grafo.agregar_arista(Arista(nodos[n1], nodos[n2]))

    return grafo

def grafoGilbert(n, p, dirigido=False):
    """Genera un grafo aleatorio según el modelo Gilbert."""
    if n <= 0:
        raise ValueError("El número de nodos debe ser mayor que 0.")
    if not (0 < p < 1):
        raise ValueError("La probabilidad p debe estar entre 0 y 1.")
    
    grafo = Grafo(dirigido)
    nodos = [Nodo(i) for i in range(n)]
    
    for nodo in nodos:
        grafo.agregar_nodo(nodo)

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                grafo.agregar_arista(Arista(nodos[i], nodos[j]))

    return grafo

def grafoGeografico(n, r, dirigido=False):
    """Genera un grafo aleatorio según el modelo geográfico."""
    if n <= 0:
        raise ValueError("El número de nodos debe ser mayor que 0.")
    if not (0 < r <= 1):
        raise ValueError("La distancia r debe estar entre 0 y 1.")
    
    grafo = Grafo(dirigido)
    posiciones = [(random.random(), random.random()) for _ in range(n)]
    nodos = [Nodo(i) for i in range(n)]
    
    for nodo in nodos:
        grafo.agregar_nodo(nodo)

    # Conectar nodos cuya distancia euclidiana es menor o igual a r
    for i in range(n):
        for j in range(i + 1, n):
             distancia = math.sqrt((posiciones[i][0] - posiciones[j][0]) ** 2 +
                                  (posiciones[i][1] - posiciones[j][1]) ** 2)
             if distancia <= r:
                grafo.agregar_arista(Arista(nodos[i], nodos[j]))
             if not dirigido:
                    grafo.agregar_arista(Arista(nodos[j], nodos[i]))

    return grafo

def grafoBarabasiAlbert(n, d, dirigido=False):
    """Genera un grafo según el modelo Barabási-Albert."""
    if n <= 0:
        raise ValueError("El número de nodos debe ser mayor que 0.")
    if d <= 1:
        raise ValueError("El grado d debe ser mayor que 1.")
    
    grafo = Grafo(dirigido)
    
    # Inicializa un grafo completo de d nodos
    nodos_iniciales = [Nodo(i) for i in range(d)]
    for nodo in nodos_iniciales:
        grafo.agregar_nodo(nodo)
    
    # Crear un grafo completamente conectado para los nodos iniciales
    for i in range(d):
        for j in range(i + 1, d):
            grafo.agregar_arista(Arista(nodos_iniciales[i], nodos_iniciales[j]))

    # Agregar nodos uno por uno
    for i in range(d, n):
        nuevo_nodo = Nodo(i)
        grafo.agregar_nodo(nuevo_nodo)

        # Selección de nodos a conectar con el nuevo nodo, basada en grados
        targets = set()
        while len(targets) < d:
            nodo_existente = random.choice(grafo.nodos)
            targets.add(nodo_existente)

        for target in targets:
            grafo.agregar_arista(Arista(nuevo_nodo, target))

    return grafo

def grafoDorogovtsevMendes(n, dirigido=False):
    """Genera un grafo según el modelo Dorogovtsev-Mendes."""
    if n < 3:
        raise ValueError("El número de nodos debe ser al menos 3.")
    
    grafo = Grafo(dirigido)
    
    # Inicializa un triángulo
    nodos_iniciales = [Nodo(i) for i in range(3)]
    for nodo in nodos_iniciales:
        grafo.agregar_nodo(nodo)
    
    grafo.agregar_arista(Arista(nodos_iniciales[0], nodos_iniciales[1]))
    grafo.agregar_arista(Arista(nodos_iniciales[1], nodos_iniciales[2]))
    grafo.agregar_arista(Arista(nodos_iniciales[0], nodos_iniciales[2]))

    # Agregar nodos adicionales conectados a una arista existente
    for i in range(3, n):
        nuevo_nodo = Nodo(i)
        grafo.agregar_nodo(nuevo_nodo)
        
        # Selección de una arista aleatoria para conectar el nuevo nodo
        arista_random = random.choice(list(grafo.aristas))
        grafo.agregar_arista(Arista(nuevo_nodo, arista_random.n1))
        grafo.agregar_arista(Arista(nuevo_nodo, arista_random.n2))

    return grafo

