import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT

class Spaceship(Sprite):
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - 40
        self.rect.y = 500

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
