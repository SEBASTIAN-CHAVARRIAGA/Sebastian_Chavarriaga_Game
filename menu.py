import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_q, MOUSEBUTTONDOWN
from game.utils.constants import SPACESHIP
import subprocess

pygame.init()

# Tamaño de la ventana del menú
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables de la nave en el menú
spaceship_image = pygame.transform.scale(SPACESHIP, (90, 100))  # Cambiar el tamaño aquí
spaceship_width, spaceship_height = spaceship_image.get_size()
spaceship_speed = 5

def show_menu():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.display.set_caption("Menu Spaceship")

    font = pygame.font.Font(None, 36)
    title_text = font.render("Spaceships Game", True, WHITE)
    start_text = font.render("Press Enter to Start", True, WHITE)
    quit_text = font.render("Press Q to Quit", True, WHITE)

    # Coordenadas iniciales de la nave en el menú
    spaceship_x = WINDOW_WIDTH // 2
    spaceship_y = WINDOW_HEIGHT // 2

    # Ángulo de rotación de la nave
    angle = 0

    running = True
    while running:
        screen.fill(BLACK)

        # Obtener la posición del cursor
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Verificar si se hizo clic izquierdo
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0]:  # botón izquierdo del mouse
            angle += 1
            if angle >= 360:
                angle = 0

        # Mover la nave hacia la posición del cursor
        dx = mouse_x - spaceship_x
        dy = mouse_y - spaceship_y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > spaceship_speed:
            # Normalizar el vector de movimiento
            dx = dx / distance
            dy = dy / distance
            # Mover la nave en la dirección normalizada
            spaceship_x += int(spaceship_speed * dx)
            spaceship_y += int(spaceship_speed * dy)
        else:
            # Si la nave está lo suficientemente cerca del cursor, llegar a las coordenadas exactas
            spaceship_x = mouse_x
            spaceship_y = mouse_y

        # Rotar la nave
        rotated_spaceship = pygame.transform.rotate(spaceship_image, angle)

        # Mostrar la nave en el menú
        spaceship_rect = rotated_spaceship.get_rect(center=(spaceship_x, spaceship_y))
        screen.blit(rotated_spaceship, spaceship_rect)

        # Mostrar el resto del menú
        screen.blit(title_text, (WINDOW_WIDTH // 2 - title_text.get_width() // 2, 200))
        screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, 300))
        screen.blit(quit_text, (WINDOW_WIDTH // 2 - quit_text.get_width() // 2, 350))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    # aquí inicia el juego
                    running = False
                    subprocess.run(["python", "main.py"])
                elif event.key == K_q:
                    # Salir del menú si se presiona la tecla "Q"
                    running = False

if __name__ == "__main__":
    show_menu()
  