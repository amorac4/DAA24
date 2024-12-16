import pygame 

class Visualizar:
    def __init__ (self, ancho, alto, radio):
        self.ancho = ancho
        self.alto = alto
        self.radio =radio
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Visualizacion de Grafo")
        self.background_color =(255, 255, 255)
        self.arista_color = (0, 0, 0)
        self.nodo_color = (0, 0, 255)

    def dibujarG(self, grafo, posicion):

        self.screen.fill(self.background_color)

        for n1, n2 in grafo.aristas:
            pygame.draw.line(self.screen, self.arista_color,posicion[n1], posicion[n2], 1)
        for nodo in grafo.nodos:
            pygame.draw.circle(self.screen, self.nodo_color, (int(posicion[nodo][0]), int(posicion[nodo][1])), self.radio)

    def actualizar(self):

        pygame.display.flip()
        
