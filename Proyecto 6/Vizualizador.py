import pygame

class Visualizar:
    def __init__(self, ancho, alto, radio):
        self.ancho = ancho
        self.alto = alto
        self.radio = radio
        self.screen = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Visualización de Grafo")
        self.fondo_color = (0, 255, 255)
        self.arista_color = (0, 255, 0)
        self.nodo_color = (128, 0, 128)

    def dibujarG(self, grafo, posicion):
        self.screen.fill(self.fondo_color)

        # Dibuja las aristas
        for nodo1, nodo2 in grafo.edges:
            try:
                pygame.draw.line(self.screen, self.arista_color,
                                 (int(posicion[nodo1][0]), int(posicion[nodo1][1])),
                                 (int(posicion[nodo2][0]), int(posicion[nodo2][1])), 1)
            except (TypeError, ValueError):
                pass