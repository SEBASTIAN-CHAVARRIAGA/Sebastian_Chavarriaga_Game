import pygame
import game_over_menu

from random import randint
from game.components.asteroids.asteroid import Asteroid

class AsteroidManager:
    def __init__(self):
        self.asteroids = pygame.sprite.Group()
        self.spawn_timer = 0

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if current_time - self.spawn_timer > 2000:  # Controla cada cuánto tiempo se crean nuevos asteroides
            x = randint(0, game.screen.get_width())
            y = 0  # Comienzan desde arriba
            speed = randint(2, 5)  # Velocidad aleatoria para los asteroides
            asteroid = Asteroid(x, y, speed)
            self.asteroids.add(asteroid)
            self.spawn_timer = current_time

        # Actualiza todos los asteroides
        self.asteroids.update()

        # Verifica si hay colisión con la nave del jugador
        if pygame.sprite.spritecollide(game.player, self.asteroids, True):
            # Reduce la vida del jugador 
            game.player_lives -= 5

            # Si el jugador se queda sin vidas, se detiene el juego
            if game.player_lives <= 0:
                    game.deaths_count += 1 
                    game_over_menu.game_over_screen(game.screen, game.score, game.max_score, game.deaths_count)

    def reset(self):
        self.asteroids.clear()

    def draw(self, screen):
        self.asteroids.draw(screen)
