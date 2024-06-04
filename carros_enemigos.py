import pygame
import random
from pygame import sprite

# Clase para los obstáculos en la pista
class Obstaculo(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, image_paths):
        super().__init__()
         # Elegir una ruta de imagen aleatoria de la lista de rutas de imagen
        image_path = random.choice(image_paths)
        # Cargar la imagen del sprite
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))  # Escalar la imagen al tamaño deseado
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        self.rect.y += self.speed
        # Eliminar el obstáculo cuando salga de la pantalla
        if self.rect.y > 800:
            self.kill()


