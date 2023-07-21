# boss.py
import pygame
import random
from game.utils.constants import BOSS, SCREEN_HEIGHT

class Boss(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.image = pygame.image.load(BOSS)
        self.rect = self.image.get_rect()
        self.rect.centery = random.randint(100, SCREEN_HEIGHT - 100)

        self.speed = 5
        self.direction = 1  # 1 derecha, -1  izquierda

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.direction *= -1
