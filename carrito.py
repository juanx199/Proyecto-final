import pygame 
import pygame.sprite

class Carrito(pygame.sprite.Sprite):
    def __init__(self, contenedor):
        super().__init__()
        self.imagenes = [pygame.image.load('imagenes/Car1.png').convert_alpha()]
        self.image = self.imagenes[0]
        self.rect = self.image.get_rect()
        self.rect.center = contenedor.get_rect().center  # Ajusta según sea necesario
        self.mask = pygame.mask.from_surface(self.image)
        self.velocidad = 5  # Velocidad del carro, ajusta según sea necesario

    def actualizar(self, direccion):
        if direccion == 'izquierda':
            self.rect.x -= self.velocidad
        elif direccion == 'derecha':
            self.rect.x += self.velocidad
        elif direccion == 'arriba':
            self.rect.y -= self.velocidad
        elif direccion == 'abajo':
            self.rect.y += self.velocidad

    def dibujar(self, superficie):
        superficie.blit(self.image, self.rect)
        
    