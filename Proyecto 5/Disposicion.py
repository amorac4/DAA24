import pygame
import math
import random
import cv2
import numpy as np
import os
from Cargador import cargarG
from Visualizar import Visualizar
from Spring import Spring

ANCHO, ALTO = 1200, 700  # Tamaño de la ventana
RADIO = 2  # Radio de los nodos
FPS = 30
m500 = "grafo_malla_500.gv"
m100 = "grafo_malla_100.gv"
ba500 ="grafo_Barabási-Albert_500_no dirigido.gv"
ba100 ="grafo_Barabási-Albert_100_no dirigido.gv"
er500 ="grafo_Erdös-Rényi_500_no dirigido.gv"
er100 ="grafo_Erdös-Rényi_100_no dirigido.gv"
geo500 ="grafo_Geográfico_500_no dirigido.gv"
geo100 ="grafo_Geográfico_100_no dirigido.gv"
gil500 ="grafo_Gilbert_500_no dirigido.gv"
gil100 ="grafo_Gilbert_100_no dirigido.gv"
do500 ="grafo_Dorogovtsev-Mendes_500_no dirigido.gv"
do100 ="grafo_Dorogovtsev-Mendes_100_no dirigido.gv"


CARPETA = "/home/verzzul/Escritorio/DAA24/Proyecto 5/Grafos/"  # Ruta a la carpeta de grafos
ARCHIVO_GRAFO = m100  # Nombre del archivo .gv a cargar


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

    # Extraer el nombre base del grafo (sin la extensión) para el video
    nombre_grafo = os.path.splitext(ARCHIVO_GRAFO)[0]
    nombre_video = os.path.join("/home/verzzul/Escritorio/DAA24/Proyecto 5/Videos", f"{nombre_grafo}.mp4")

    # Cargar el grafo
    grafo = cargarG(ruta_archivo)
    if grafo is None:
        print("Error al cargar el grafo. Verifique la ruta y el archivo.")
        return

    # Inicialización de posiciones
    posiciones = posiciones_iniciales_mixtas(grafo.nodes, ANCHO, ALTO)
    viz = Visualizar(ANCHO, ALTO, RADIO)

    # Configuración del algoritmo Spring
    spring = Spring(grafo, posiciones, ANCHO, ALTO, repulsion=1, atraccion=0.02, amortiguacion=0.85)

    # Configuración del archivo de video
    print(f"Guardando video como: {nombre_video}")
    video_salida = cv2.VideoWriter(nombre_video, cv2.VideoWriter_fourcc(*'mp4v'), FPS, (ANCHO, ALTO))

    # Bucle principal: sigue iterando hasta que se cierre la ventana
    running = True
    clock = pygame.time.Clock()
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
    print(f"Video guardado como: {nombre_video}")

if __name__ == "__main__":
    main()