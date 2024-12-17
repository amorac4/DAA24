import pygame
import math
import random
import cv2
import numpy as np
import os
from Cargador import cargarG
from Visualizar import Visualizar
from Spring import Spring

ANCHO, ALTO = 800, 600  # Tamaño de la ventana
RADIO = 5  # Radio de los nodos
FPS = 30
m500 = ""
m100 = "grafo_malla_100.gv"
ba500 =""
ba100 ="grafo_Barabási-Albert_100_no dirigido.gv"
er500 =""
er100 ="grafo_Erdös-Rényi_100_no dirigido.gv"
geo500 =""
geo100 ="grafo_Geográfico_100_no dirigido.gv"
gil500 =""
gil100 ="grafo_Gilbert_100_no dirigido.gv"
do500 =""
do100 ="grafo_Dorogovtsev-Mendes_100_no dirigido.gv"


CARPETA = "/home/verzzul/Escritorio/DAA24/Proyecto 5/Grafos/"  # Ruta a la carpeta de grafos
ARCHIVO_GRAFO = do100  # Nombre del archivo .gv a cargar


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
    clock = pygame.time.Clock()
    video_salida = cv2.VideoWriter("/home/verzzul/Escritorio/DAA24/Proyecto 5/Videos/salida_grafo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), FPS, (ANCHO, ALTO))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        spring.run(iteraciones=1)  # Ejecuta el algoritmo Spring paso a paso
        viz.dibujarG(grafo, spring.posiciones)  # Redibuja el grafo
        # Capturar la pantalla y guardar el fotograma en el video
        captura = pygame.surfarray.array3d(pygame.display.get_surface())
        captura = np.transpose(captura, (1, 0, 2))  # OpenCV necesita el formato correcto
        video_salida.write(cv2.cvtColor(captura, cv2.COLOR_RGB2BGR))

        clock.tick(FPS)

    # Cerrar OpenCV y Pygame
    video_salida.release()

    pygame.quit()
    print("Video guardado como output.mp4")

if __name__ == "__main__":
    main()
