import pygame
import sys
import random
from carros_enemigos import Obstaculo

def iniciar_pygame():
    # Inicializar Pygame
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    Vidas = 1
    Puntaje = 0
    
    # Dimensiones de la ventana
    screen_width = 800
    screen_height = 600

    # Crear la ventana del juego
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Highway Rush")
    
    #+++ textico
    # Establecer la fuente y el tamaño del texto
    font = pygame.font.Font(None, 37)
    font2 = pygame.font.Font(None, 100)

    # Crear textos
    #texto_vidas = font.render("Vidas: " + str(Vidas), True, BLACK) #oculto
    texto_puntaje = font.render("Puntaje: " + str(Puntaje), True, BLACK)
    texto_derrota1 = font2.render("Has Perdido", True, BLACK)
    texto_derrota2 = font2.render("Tu Puntaje: " + str(Puntaje), True, BLACK)

    # Obtener rectangulos de textos
    #text_vidas_rect = texto_vidas.get_rect(topleft=(10, 25)) #oculto
    text_Puntaje_rect = texto_puntaje.get_rect(topleft=(10, 25))
    text_derrota1_rect = texto_derrota1.get_rect(topleft=(170, 200))
    text_derrota2_rect = texto_derrota2.get_rect(topleft=(160, 400))
    #+++ textico

    # Cargar la imagen de la carretera
    background = pygame.image.load('imagenes/carretera.jpeg')

    # Inicializar la posición vertical de la carretera
    background_y = 0

    # Cargar la imagen del carro
    car = pygame.image.load('imagenes/Car1.png')
    car_width, car_height = car.get_size()  # Obtener el ancho y alto del carro

    # Posición inicial del carro
    car_x = screen_width // 2 - car_width // 2
    car_y = screen_height - car_height - 20

    # Ángulo de rotación inicial del carro
    angle = 0

    # Velocidad de movimiento del fondo de la carretera y del carro
    speed = 10
    car_speed = 5

    # Reloj para controlar la velocidad de fotogramas
    clock = pygame.time.Clock()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    # Configuración de generación de obstáculos
    obstacle_frequency = 20
    obstacle_counter = 0

    # Lista de rutas de imagen para los obstáculos
    obstacle_image_paths = [
        'imagenes/car1.png', 'imagenes/car2.png', 'imagenes/car3.png', 
        'imagenes/car4.png', 'imagenes/car5.png', 'imagenes/car6.png', 
        'imagenes/car7.png', 'imagenes/car8.png'
    ]

    # Crear un rectángulo para el carro del jugador (necesario para detectar colisiones)
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mover la carretera hacia abajo
        background_y += speed
        if background_y > screen_height:
            background_y = 0

        # Mover el carro y ajustar el ángulo de rotación
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            car_x -= car_speed
            angle = 10  # Ángulo de rotación para la izquierda
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            car_x += car_speed
            angle = -10  # Ángulo de rotación para la derecha
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            car_y -= car_speed
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            car_y += car_speed
        else:
            angle = 0  # No hay rotación si no se presionan las teclas de dirección

        # Limitar la posición del carro para que no salga de la pantalla
        car_x = max(0, min(car_x, screen_width - car_width))
        car_y = max(0, min(car_y, screen_height - car_height))

        # Actualizar el rectángulo del carro del jugador
        car_rect.topleft = (car_x, car_y)

        # Generación de obstáculos
        obstacle_counter += 1
        if obstacle_counter == obstacle_frequency:
            obstacle_width = 50
            obstacle_height = 60
            obstacle_speed = random.randint(5, 9)
            obstacle_x = random.randint(90, 700 - obstacle_width)
            obstacle = Obstaculo(obstacle_x, -50, obstacle_width, obstacle_height, obstacle_speed, obstacle_image_paths)
            all_sprites.add(obstacle)
            obstacles.add(obstacle)
            obstacle_counter = 0

        # Actualizar la lógica del juego
        all_sprites.update()

        # Crear un sprite temporal con el rectángulo del carro del jugador
        temp_sprite = pygame.sprite.Sprite()
        temp_sprite.rect = car_rect

        for obs in obstacles:
            if obs.rect.y > car_y + car_height:  # Si el obstáculo está más abajo que el carro
                Puntaje += 1
                texto_puntaje = font.render("Puntaje: " + str(Puntaje), True, BLACK)

        # Comprobar colisiones   
        if pygame.sprite.spritecollideany(temp_sprite, obstacles):
            Vidas -= 1
            # Renderizar el texto actualizado de la energía
            texto_vidas = font.render("Vidas: " + str(Vidas), True, BLACK)
            if Vidas <= 0:
                texto_derrota1 = font2.render("Has Perdido", True, BLACK)
                texto_derrota2 = font2.render("Tu Puntaje: " + str(Puntaje), True, BLACK)
                screen.blit(texto_derrota1, text_derrota1_rect)
                screen.blit(texto_derrota2, text_derrota2_rect)
                pygame.display.flip()
                pygame.time.delay(5000)
                running = False  # Termina el juego si la energía llega a 0

        # Dibujar la carretera en la pantalla
        screen.fill((0, 0, 0))  # Limpiar la pantalla
        screen.blit(background, (0, background_y))
        screen.blit(background, (0, background_y - screen_height))

        # Rotar la imagen del carro
        rotated_car = pygame.transform.rotate(car, angle)

        # Dibujar el carro rotado en la pantalla
        screen.blit(rotated_car, (car_x, car_y))

        # Dibujar los obstáculos
        all_sprites.draw(screen)
        
        # Dibujar el texto en la pantalla
        #screen.blit(texto_vidas, text_vidas_rect) #oculto
        screen.blit(texto_puntaje, text_Puntaje_rect)
        # Actualizar la pantalla
        pygame.display.flip()
        
        # velocidad de fotogramas
        clock.tick(60)

    pygame.quit()
    sys.exit()