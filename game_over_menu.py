import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN

# Constantes de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def game_over_screen(screen, score, max_score, deaths_count):
    font = pygame.font.Font(None, 36)
    title_text = font.render("Game Over", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    max_score_text = font.render(f"Max Score: {max_score}", True, WHITE)
    deaths_text = font.render(f"Deaths: {deaths_count}", True, WHITE)
    instructions_text = font.render("Press Enter to Play Again", True, WHITE)

    # Centrar el texto en la pantalla
    screen_rect = screen.get_rect()
    title_text_rect = title_text.get_rect(center=(screen_rect.centerx, 200))
    score_text_rect = score_text.get_rect(center=(screen_rect.centerx, 250))
    max_score_text_rect = max_score_text.get_rect(center=(screen_rect.centerx, 300))
    deaths_text_rect = deaths_text.get_rect(center=(screen_rect.centerx, 350))
    instructions_text_rect = instructions_text.get_rect(center=(screen_rect.centerx, 450))

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(title_text, title_text_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(max_score_text, max_score_text_rect)
        screen.blit(deaths_text, deaths_text_rect)
        screen.blit(instructions_text, instructions_text_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    running = False
