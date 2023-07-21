import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_1, ASTEROID_2
from random import randint

class Asteroid(Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.original_image = ASTEROID_1 if randint(0, 1) == 0 else ASTEROID_2
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.angle = 0

    def update(self):
        self.rect.y += self.speed
        self.angle = (self.angle + 2) % 360  # Incrementa el ángulo de rotación en cada actualización (ajusta según el giro deseado)
        self.rotate()

        # Si el asteroide sale completamente de la pantalla por la parte inferior
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.bottom = 0  # Aparecer en la parte superior nuevamente

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
