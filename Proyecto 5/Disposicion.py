import pygame
import math
import random
import os
from Cargador import cargarG
from Visualizar import Visualizar
from Spring import Spring

ANCHO, ALTO = 800, 600  # Tamaño de la ventana
RADIO = 5  # Radio de los nodos
CARPETA = "/home/verzzul/Escritorio/DAA24/Proyecto 5/Grafos/"  # Ruta a la carpeta de grafos
ARCHIVO_GRAFO = "grafo_malla_100.gv"  # Nombre del archivo .gv a cargar

def posiciones_iniciales_mixtas(nodos, ancho, alto):
    """
    Distribuye los nodos en una espiral con ruido aleatorio, dentro de los límites.
    """
    centro_x, centro_y = ancho // 2, alto // 2
    espaciado = 20
    posiciones = {}
    angulo = 0
    radio = 0

    for i, nodo in enumerate(nodos):
        x = max(50, min(ancho - 50, centro_x + int(radio * math.cos(angulo)) + random.randint(-50, 50)))
        y = max(50, min(alto - 50, centro_y + int(radio * math.sin(angulo)) + random.randint(-50, 50)))
        posiciones[nodo] = (x, y)
        angulo += math.pi / 8
        radio += espaciado
    return posiciones

def main():
    # Construir la ruta completa del archivo .gv
    ruta_archivo = os.path.join(CARPETA, ARCHIVO_GRAFO)

    # Cargar el grafo
    grafo = cargarG(ruta_archivo)

    if grafo is None:
        print("Error al cargar el grafo. Verifique la ruta y el archivo.")
        return

    # Inicialización de posiciones
    posiciones = posiciones_iniciales_mixtas(grafo.nodes, ANCHO, ALTO)
    viz = Visualizar(ANCHO, ALTO, RADIO)

    # Configuración del algoritmo Spring
    spring = Spring(grafo, posiciones, ANCHO, ALTO, repulsion=2, atraccion=0.01, amortiguacion=0.85)

    # Bucle principal: sigue iterando hasta que se cierre la ventana
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        spring.run(iteraciones=1)  # Ejecuta el algoritmo Spring paso a paso
        viz.dibujarG(grafo, spring.posiciones)  # Redibuja el grafo

    pygame.quit()

if __name__ == "__main__":
    main()
