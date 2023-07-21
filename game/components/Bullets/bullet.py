import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET,BULLET_ENEMY,SCREEN_HEIGHT

class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET,(25, 35))
    BULLET_SIZE_ENEMY = pygame.transform.scale(BULLET_ENEMY,(9,32))
    BULLETS = {'player' : BULLET_SIZE, 'enemy': BULLET_SIZE_ENEMY}
    SPEED = 20
    def __init__(self, spacechip):
        self.image = self.BULLETS[spacechip.type]
        self.rect = self.image.get_rect()
        self.rect.center = spacechip.rect.center
        self.owner = spacechip.type


    def update(self, bullets):
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
        else:
            self.rect.y -= self.SPEED
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)

 

    def draw(self, screen):
        screen.blit(self.image, self.rect)