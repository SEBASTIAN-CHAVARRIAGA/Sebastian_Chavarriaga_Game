import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT

class Spaceship(Sprite):
    SHIP_WITH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_HEIGHT // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        if user_input[pygame.K_a]:
            self.rect.x -= 10
            if self.rect.right < 0:
                self.rect.x = SCREEN_WIDTH
        if user_input[pygame.K_d]:
            self.rect.x += 10
            if self.rect.left > SCREEN_WIDTH:
                self.rect.x = -self.rect.width

        if self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

        if user_input[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 10
        if user_input[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10

        if user_input[pygame.K_a] and user_input[pygame.K_w]:
            self.rect.x -= 10
            self.rect.y -= 10
            if self.rect.right < 0:
                self.rect.x = SCREEN_WIDTH
            if self.rect.top < 0:
                self.rect.y = 0
        if user_input[pygame.K_a] and user_input[pygame.K_s]:
            self.rect.x -= 10
            self.rect.y += 10
            if self.rect.right < 0:
                self.rect.x = SCREEN_WIDTH
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.y = SCREEN_HEIGHT - self.rect.height
        if user_input[pygame.K_d] and user_input[pygame.K_w]:
            self.rect.x += 10
            self.rect.y -= 10
            if self.rect.left > SCREEN_WIDTH:
                self.rect.x = -self.rect.width
            if self.rect.top < 0:
                self.rect.y = 0
        if user_input[pygame.K_d] and user_input[pygame.K_s]:
            self.rect.x += 10
            self.rect.y += 10
            if self.rect.left > SCREEN_WIDTH:
                self.rect.x = -self.rect.width
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.y = SCREEN_HEIGHT - self.rect.height

    def draw(self, screen):
        screen.blit(self.image, self.rect)
