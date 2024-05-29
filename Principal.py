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


ROJO = (255, 0, 0)
VERDE_CLARO = (144, 238, 144)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NARANJA = (255, 165, 0)
AMARILLO = (255, 255, 0)
AZUL = (0, 0, 139)


#ruta_abs = os.path.abspath("Imagenes\MenuInicio.jpg")
 
root = tk.Tk()
root.title('Highway Rush')
root.geometry = ('1000x600')

###########################################################



ruta_fondo = 'C:/Users/lenovo/Dropbox/PP/FINAL/Imagenes/MenuInicio20.jpg'
ruta_logo = 'C:/Users/lenovo/Dropbox/PP/FINAL/Imagenes/Logo.png'

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
    image = Image.open(ruta_logo)
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
boton_jugar.place(x=700, y=300)

root.mainloop()


##################################################################
Clock = pygame.time.Clock()


userName = str
points = 0
date = str
speed = 5
first = True
fullscreen = False


