import sys
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import font
from carrito import *

# Se cargan las rutas de las imagenes
ruta_juego = 'imagenes/carretera.jpeg'
ruta_fondo = 'imagenes/menu_inicio.jpeg'
ruta_logo = 'imagenes/Logo.jpg'
ruta_fuente = 'ruta/a/8-bit Arcade In.ttf' 

# Creacion de la ventana
root = tk.Tk()
root.title('Highway Rush')
root.geometry('800x920')

# Se carga la imagen de fondo
try:
    image = Image.open(ruta_fondo)
    background_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    sys.exit(1)

# Creacion del canvas fondo
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")
canvas.image = background_image

# Cargar la imagen y apalicar filtro
try:
    fondo_jugar = Image.open(ruta_juego)
    distorted_image = fondo_jugar.filter(ImageFilter.BLUR)
    distorted_image_tk = ImageTk.PhotoImage(distorted_image)
except Exception as e:
    print(f"Error al cargar la imagen del juego: {e}")
    sys.exit(1)

# Se carga el logo
try:
    image = Image.open(ruta_logo)
    logo_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen del logo: {e}")
    sys.exit(1)

root.call('wm', 'iconphoto', root._w, logo_image)

# Se carga la fuente
try:
    custom_font = font.Font(family="8-bit Arcade In", size=16)
except Exception as e:
    print(f"Error al cargar la fuente personalizada: {e}")
    custom_font = ("Arial", 16)  # Fuente de respaldo por si no funciona la personalizada

def jugar():
    boton_jugar.place_forget()
    boton_salir.place_forget()
    boton_iniciar.place_forget()
    # Botones y coordenadas
    nombre_label.place(x=490, y=500)
    nombre_entry.place(x=490, y=540)
    boton_iniciar.place(x=490, y=580)

def iniciar_juego():
    nombre = nombre_entry.get()
    nombre_label.place_forget()
    nombre_entry.place_forget()
    boton_iniciar.place_forget()
    boton_salir.place_forget()
    boton_iniciar.place_forget()

    if nombre:
        # Borrar el canvas
        canvas.delete("all")
        canvas.create_image(0, 0, image=distorted_image_tk, anchor="nw")
        mensaje = canvas.create_text(400, 460, text=f"Bienvenido, {nombre}! El juego comienza ahora.", fill="black", font=("8-bit Arcade In", 30))

        root.after(5000, lambda: canvas.delete(mensaje))

    def cuenta_regresiva(contador):
        if contador > 0:
            canvas.delete("contador")
            canvas.create_text(400, 460, text=str(contador), fill="black", font=("8-bit Arcade In", 100), tag="contador")
            root.after(1000, lambda: cuenta_regresiva(contador - 1))
        else:
            canvas.delete("contador")
            canvas.create_text(400, 460, text="START!", fill="black", font=("8-bit Arcade In", 110))
            root.after(1000, lambda: [root.destroy(), iniciar_pygame()])  # Cerrar la ventana de Tkinter y ejecutar iniciar_pygame

    root.after(5000, lambda: cuenta_regresiva(5))
    

def salir():
    root.quit()

VERDE_CLARO = "#399183"
nombre_label = tk.Label(root, text="Ingrese su nombre:", font=custom_font)
nombre_entry = tk.Entry(root, font=custom_font)
boton_iniciar = tk.Button(root, text="Iniciar juego", command=iniciar_juego, font=custom_font, bd=3, fg="black", bg= VERDE_CLARO, width=14, height=2)

boton_jugar = tk.Button(root, text="JUGAR", command=jugar, font=custom_font, bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_jugar.place(x=490, y=500)

boton_salir = tk.Button(root, text="SALIR", command=salir, font=custom_font, bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_salir.place(x=490, y=560)

root.mainloop()
