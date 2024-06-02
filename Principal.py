import pygame
import sys
#import Carros_enemigos
from pygame.locals import *
#import random
#import json
from datetime import datetime
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import simpledialog
import customtkinter as CTk
from carrito import Carrito

pygame.init() 
 

ROJO = (255, 0, 0)
VERDE_CLARO = (144, 238, 144)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 165, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 139)


ruta_abs = ("Imagenes\Menu_inicio.jpg") 

 
root = tk.Tk()
root.title('Highway Rush')
root.geometry = ('40x60')

###########################################################


ruta_fondo = 'Imagenes\menu_inicio.jpeg' 
 

try:
    image = Image.open(ruta_fondo)
    background_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit(1)

# Crear un canvas para poner la imagen de fondo
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0, 0, image=background_image, anchor="nw")

canvas.image = background_image

try:
    image = Image.open(ruta_fondo)
    background_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit(1)


root.call('wm', 'iconphoto', root._w, background_image)

def jugar():
    # Solicitar el nombre del usuario
    nombre = tk.simpledialog.askstring("Nombre", "Por favor, ingrese su nombre:")

    # Verificar que el nombre no esté vacío
    if nombre:
        iniciar_juego(nombre)

def iniciar_juego(nombre):
    # Limpiar el canvas
    canvas.delete("all")

    canvas.create_text(400, 300, text=f"Bienvenido, {nombre}! El juego comienza ahora.", fill="black", font=("8-bit Arcade In", 24))

nombre_label = tk.Label(root, text="Ingrese su nombre:", font=("8-bit Arcade In", 12))
nombre_entry = tk.Entry(root, font=("8-bit Arcade In", 12))
boton_iniciar = tk.Button(root, text="Iniciar juego", command=iniciar_juego, font=("8-bit Arcade In", 12), bd=2, fg="white", bg="green", width=14, height=2)


VERDE_CLARO = "#399183"
boton_jugar = tk.Button(text="JUGAR", command=jugar, font=("8-bit Arcade In", 16), bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_jugar.place(x=520, y=450)

root.mainloop()



Clock = pygame.time.Clock()


userName = str
points = 0
date = str
speed = 5
first = True
fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Maneja otros eventos como el teclado

    # Actualiza el estado del carrito del usuario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        carrito_usuario.actualizar('izquierda')
    if keys[pygame.K_RIGHT]:
        carrito_usuario.actualizar('derecha')
    if keys[pygame.K_UP]:
        carrito_usuario.actualizar('arriba')
    if keys[pygame.K_DOWN]:
        carrito_usuario.actualizar('abajo')

    # Dibuja el carrito del usuario en la pantalla
    # Asumiendo que 'pantalla' es la superficie donde dibujas tu juego en Pygame
    pantalla.fill((0, 0, 0))  # Rellena la pantalla con negro
    carrito_usuario.dibujar(pantalla)
    pygame.display.flip()
    Clock.tick(60)  # Limita el framerate a 60 FPS