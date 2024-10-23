
from bfs import BFS
from dfs_r import DFS_Recursivo
from dfs_i import DFS_ITERATIVO
from Generador import GenGrafo

def elegir_grafo():

    print("\nSeleccione el tipo de grafo que desea generar:")
    print("1. Grafo de Malla")
    print("2. Grafo de Erdos-Reny")
    print("3. Grafo de Gilbert")
    print("4. Grafo de Geografico")
    print("5. Grafo de Barabasi-Albert")
    print("6. Grafo de Dorogovtsev-Mendes")

    opcion= input ("Ingrese el numero de grafo")
    return opcion


def iniciar_busquda():

    opcion = elegir_grafo()

    if opcion =='1':

        filas = int(input("Ingrese el nuero de filas"))
        columnas = int(input("Ingrese el nuero de columnas"))
        generador = GenGrafo(filas*columnas)
        grafo = generador.crear_y_mostrar_grafo(grafo_func=lambda n: grafoMalla(filas, columnas), nombre="Malla")

    elif opcion =='2':

        filas = int(input("Ingrese el nuero de filas"))
        columnas = int(input("Ingrese el nuero de columnas"))
        generador = GenGrafo(filas*columnas)
        grafo = generador.crear_y_mostrar_grafo(grafo_func=lambda n: grafoMalla(filas, columnas), nombre="Malla")