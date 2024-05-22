import pygame
import sys
#import Carros_enemigos
from pygame.locals import *
#import random
import json
from datetime import datetime
#from customtkinter import CTk    el tkinter no me deja unirlo con la imagen de inicio preguntar al profesor

Clock = pygame.time.Clock()


background_image = pygame.image.load("Imagenes/Menu_inicio.jpg")

size = width, height = 800, 500
pygame.display.set_caption("Highway Rush")

#Colores a utilizar (caso con el menu)
RED = (255, 0, 0)
GREEN = (20, 255, 140)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NARANJA = (255, 165, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 139)

userName = str
points = 0
date = str
speed = 5
first = True
fullscreen = False
# Mirando fuentes para la creacion de botones
bit = pygame.font.SysFont("8-bit Arcade In", 30)
fuente = bit.render("Codigo", 0, AZUL)

#creando el inicio de la pantalla
def main():
    pygame.init()
    screen = pygame.display.set_mode((800,500))
    background_image = pygame.image.load("Imagenes/Menu_inicio.jpg")
    background_rect = background_image.get_rect()
    running = True

    while running:
        screen.blit(background_image, background_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    
    pygame.quit()
    sys.exit()