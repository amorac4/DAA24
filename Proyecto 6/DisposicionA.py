import pygame
import math
import random
import cv2
import numpy as np
import os
from CargadorG import cargarG
from Vizualizador import Visualizar
from Spring import Spring
from FruchtermanReingold import FruchtermanReingold
from BarnesHut import BarnesHut

ANCHO, ALTO = 1200, 700  # Tamaño de la ventana
RADIO = 4  # Radio de los nodos
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
    nombre_video = os.path.join("/home/verzzul/Escritorio/DAA24/Proyecto 6/Videos", f"{nombre_grafo}.mp4")

    # Cargar el grafo
    grafo = cargarG(ruta_archivo)
    if grafo is None:
        print("Error al cargar el grafo. Verifique la ruta y el archivo.")
        return
    
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Disposición del Grafo")

    # Inicialización de posiciones
    posiciones = posiciones_iniciales_mixtas(grafo.nodes, ANCHO, ALTO)
    viz = Visualizar(ANCHO, ALTO, RADIO)

    #seleccion de algoritmo
    print("seleccionar el algoritmo de disposicion:")
    print("1. Spring")
    print("2. Fruchterman-Reingold")
    print("3. Barnes-Hut")
    opcion =input("Elija una opcion:")

    if opcion == "1":
        algoritmo = Spring(grafo, posiciones, ANCHO, ALTO, repulsion=1, atraccion=0.02, amortiguacion=0.85)
    elif opcion == "2":
        algoritmo = FruchtermanReingold(grafo, posiciones, ANCHO, ALTO, repulsion=30, atraccion=0.01, amortiguacion=0.9)
    elif opcion == "3":
        algoritmo = BarnesHut(0, ANCHO, 0, ALTO, theta=0.5, repulsion=450,atraccion=0.8 , min_distancia=5)
        objetos = {nodo: (posiciones[nodo][0], posiciones[nodo][1]) for nodo in grafo.nodes}
        algoritmo.construirQ(objetos)
    else:
        print("opcion invalidad")
        return

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
                
        pantalla.fill((0, 255, 255))

        if opcion == "3":
            posiciones = algoritmo.ActuPos(grafo, posiciones)

        else:
            algoritmo.run(iteraciones=1)  # Ejecuta el algoritmo Selecionado paso a paso
        
        viz.dibujarG(grafo, algoritmo.posiciones)  # Redibuja el grafo

         # Dibuja el Quadtree (opcional para depuración)
        if opcion == "3":  # Solo si se está usando Barnes-Hut
            algoritmo.dibujar_quadtree(pantalla)

        # Actualiza la ventana
        pygame.display.flip()
        

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