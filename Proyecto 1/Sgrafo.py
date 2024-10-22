import random
import math
from Snodo import Nodo
from Sarista import Arista

# Clase Grafo para representar un grafo con nodos y aristas.
class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = [] #lista  nodos en el grafo
        self.aristas = set()#Conjunto de aristas en el grafo
        self.dirigido = dirigido # Indiga si el grafo es dirigido o no

    def agregar_nodo(self, nodo):
        # Agrega un nodo al grafo
        self.nodos.append(nodo)

    def existe_arista(self, arista):
        # Verifica si la arista ya existe en el grafo.
        if self.dirigido:
            return arista in self.aristas
        else:
            return arista in self.aristas or Arista(arista.n2, arista.n1) in self.aristas

    def agregar_arista(self, arista):
        #Agrega una arista si no existe ya en el grafo
        if not self.existe_arista(arista):
            self.aristas.add(arista)
            arista.n1.aristas.add(arista) #Añade la arista al nodo n1
            arista.n2.aristas.add(arista) #Añade la arista al nodo n2
            return True
        return False

    def guardar_graphviz(self, filename):
        #Guarda el grafo en formato .dot para usar con Graphviz.
        with open(filename, 'w') as f:
            f.write("digraph G {\n" if self.dirigido else "graph G {\n")
            for arista in self.aristas:
                if self.dirigido:
                    f.write(f'    "{arista.n1.id}" -> "{arista.n2.id}";\n')
                else:
                    f.write(f'    "{arista.n1.id}" -- "{arista.n2.id}";\n')
            f.write("}\n")

    def mostrar_grafo(self):
        #imprime la estructuta del grafo, indicando si es dirigido o no, y el numero de nodos y aristas
        print(f"Grafo {'dirigido' if self.dirigido else 'no dirigido'} con {len(self.nodos)} nodos y {len(self.aristas)} aristas.")

def generar_nodos(n, nombre_prefix="n"):
    #Genera n nodos con un prefijo de nombre.
    #Retorna una lista de objetos Nodo con identificadores unicos.
    return [Nodo(f"{nombre_prefix}{i}") for i in range(n)]

# Genera un grafo de malla de tamaño m x n.
# Conecta cada nodo con sus vecinos inmediatos en una estructura rectangular.
def grafoMalla(m, n, dirigido=False):
    
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

# Genera un grafo aleatorio según el modelo Erdös-Rényi.
# Crea n nodos y m aristas aleatorias.
def grafoErdosRenyi(n, m, dirigido=False):

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


# Genera un grafo aleatorio según el modelo Gilbert.
# Crea un grafo donde cada par de nodos está conectado con una probabilidad p.
def grafoGilbert(n, p, dirigido=False):
    
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


# Genera un grafo aleatorio según el modelo geográfico.
# Conecta nodos que se encuentran dentro de una distancia r en un plano unitario.
def grafoGeografico(n, r, dirigido=False):
    
    if n <= 0:
        raise ValueError("El número de nodos debe ser mayor que 0.")
    if not (0 < r <= 1):
        raise ValueError("La distancia r debe estar entre 0 y 1.")
    
    grafo = Grafo(dirigido)
    posiciones = [(random.random(), random.random()) for _ in range(n)] # Asigna posiciones aleatorias a los nodos.
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


# Genera un grafo aleatorio con el modelo Barabási-Albert.
# Cada nuevo nodo se conecta a d nodos ya existentes con una probabilidad proporcional al grado de los nodos existentes.
def grafoBarabasiAlbert(n, d, dirigido=False, auto=False):
    
    if n < 1 or d < 2:
        raise ValueError("Error: n > 0 y d > 1")
    
    grafo = Grafo(dirigido)
    nodos_deg = dict() # Diccionario para llevar el conteo del grado de cada nodo.
    
    # Crear nodos
    for nodo_id in range(n):
        nodo = Nodo(nodo_id)
        grafo.agregar_nodo(nodo)
        nodos_deg[nodo_id] = 0
    
    nodos = grafo.nodos
    
    # Agregar aristas al azar, con cierta probabilidad
    for nodo in nodos:
        for v in nodos:
            if nodos_deg[nodo.id] == d:
                break
            if nodos_deg[v.id] == d:
                continue
            p = random.random()
            equal_nodes = v == nodo
            if equal_nodes and not auto:
                continue

            if p <= 1 - nodos_deg[v.id] / d and grafo.agregar_arista(Arista(nodo, v)):
                nodos_deg[nodo.id] += 1
                if not equal_nodes:
                    nodos_deg[v.id] += 1

    return grafo



# Genera un grafo según el modelo Dorogovtsev-Mendes.
# Inicia con un triángulo y agrega nodos que se conectan a una arista existente.
def grafoDorogovtsevMendes(n, dirigido=False):
    
    if n < 3:
        raise ValueError("El número de nodos debe ser al menos 3.")
    
    grafo = Grafo(dirigido)
    
    # Inicializa un triángulo
    nodos_iniciales = [Nodo(i) for i in range(3)]
    for nodo in nodos_iniciales:
        grafo.agregar_nodo(nodo)
    
    # Conectar los nodos iniciales en un triángulo.
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

