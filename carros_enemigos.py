import pygame
import os
import json
from pygame.sprite import _Group

class Carros_enemigos(pygame.sprite.Sprite):

    def __init__(self, tipo, carril):
        super.__init__()

        global speed

        self.size(50, 50)
        #confirmar el tamaño de la imagen y su posicion
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(directory + "\\Imagenes\\Car1.png").convert_alpha(),self.size),180)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.tipo = tipo
        self.carretera = carril

#estoy terminando el codigo#  
