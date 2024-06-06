import sys
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
from tkinter import font
from carrito import iniciar_pygame

# Ruta de las imágenes
ruta_juego = 'imagenes/carretera.jpeg'
ruta_fondo = 'imagenes/menu_inicio.jpeg'
ruta_logo = 'imagenes/Logo.jpg'
ruta_fuente = 'ruta/a/8-bit Arcade In.ttf'  # Cambia esto a la ruta de tu fuente

# Inicializar la ventana de Tkinter
root = tk.Tk()
root.title('Highway Rush')
root.geometry('800x920')

# Cargar la imagen de fondo
try:
    image = Image.open(ruta_fondo)
    background_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen de fondo: {e}")
    sys.exit(1)

# Crear un canvas para poner la imagen de fondo
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")
canvas.image = background_image

# Cargar imagen de juego con filtro
try:
    fondo_jugar = Image.open(ruta_juego)
    distorted_image = fondo_jugar.filter(ImageFilter.BLUR)
    distorted_image_tk = ImageTk.PhotoImage(distorted_image)
except Exception as e:
    print(f"Error al cargar la imagen del juego: {e}")
    sys.exit(1)

# Cargar el logo
try:
    image = Image.open(ruta_logo)
    logo_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen del logo: {e}")
    sys.exit(1)

root.call('wm', 'iconphoto', root._w, logo_image)

# Registrar la fuente personalizada
try:
    custom_font = font.Font(family="8-bit Arcade In", size=16)
except Exception as e:
    print(f"Error al cargar la fuente personalizada: {e}")
    custom_font = ("Arial", 16)  # Fuente de respaldo

def jugar():
    boton_jugar.place_forget()
    boton_salir.place_forget()
    boton_iniciar.place_forget()
    boton_guardar.place.forget()
    # Mostrar los campos de entrada y botón en el canvas
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
    boton_guardar.place.forget()

    if nombre:
        # Limpiar el canvas
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
            root.after(1000, iniciar_pygame)

    root.after(5000, lambda: cuenta_regresiva(5))
    
def guardar_puntaje():
    nombre = nombre_entry.get()
    puntaje = 100  # Aquí debes calcular el puntaje del jugador

    # Guardar el nombre y el puntaje en un archivo o base de datos
    with open("puntajes.txt", "a") as archivo:
        archivo.write(f"{nombre}: {puntaje}\n")

def salir():
    root.quit()

VERDE_CLARO = "#399183"
nombre_label = tk.Label(root, text="Ingrese su nombre:", font=custom_font)
nombre_entry = tk.Entry(root, font=custom_font)
boton_iniciar = tk.Button(root, text="Iniciar juego", command=iniciar_juego, font=custom_font, bd=3, fg="black", bg= VERDE_CLARO, width=14, height=2)

boton_jugar = tk.Button(root, text="JUGAR", command=jugar, font=custom_font, bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_jugar.place(x=490, y=500)

boton_guardar = tk.Button(root, text="SCORE", command=guardar_puntaje, font=("8-bit Arcade In", 16), bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_guardar.place(x=490, y=560)

boton_salir = tk.Button(root, text="SALIR", command=salir, font=custom_font, bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_salir.place(x=490, y=620)

root.mainloop()
