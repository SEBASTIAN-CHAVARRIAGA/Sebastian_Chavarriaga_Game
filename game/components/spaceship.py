import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_WIDTH, SCREEN_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT, DEFAULT_TYPE
from game.components.Bullets.bullet import Bullet

class Spaceship(Sprite):
    SHIP_WITH = 40
    SHIP_HEIGHT = 60
    COOLDOWN_TIME = 10000  

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image, (SHIP_WIDTH, SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH // 2) - 40
        self.rect.y = 500
        self.angle = 0
        self.rotating = False
        self.last_rotate_time = 0
        self.bullet_cooldown = 500  
        self.last_shot_time = 0
        self.type = 'player'
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0
    def update(self, user_input, player_bullets):
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

        current_time = pygame.time.get_ticks()
        if user_input[pygame.K_SPACE] and current_time - self.last_rotate_time >= self.COOLDOWN_TIME:
            self.rotate(current_time)

        current_time = pygame.time.get_ticks()
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0] and current_time - self.last_shot_time >= self.bullet_cooldown:
            self.shoot(player_bullets, current_time)

    def rotate(self, current_time):
        self.rotating = True
        self.last_rotate_time = current_time


    def shoot(self, player_bullets, current_time):
        bullet = Bullet(self)
        player_bullets.add(bullet)
        game.bullet_manager.add_bullet(bullet)  # Agregar la bala al BulletManager
        self.last_shot_time = current_time

   
    def set_image(self, size = (40, 60), image = SPACESHIP):
                  self.image = image
                  self.image = pygame.transform.scale(self.image, size)

    def draw(self, screen):
        if self.rotating:
            self.angle += 10
            if self.angle >= 360:
                self.angle = 0
                self.rotating = False
            rotated_image = pygame.transform.rotate(self.image, self.angle)
            new_rect = rotated_image.get_rect(center=self.rect.center)
            screen.blit(rotated_image, new_rect)
        else:
            screen.blit(self.image, self.rect)

        # Indicador de habilidad esquina superior izquierda
        remaining_cooldown = max(0, self.COOLDOWN_TIME - (pygame.time.get_ticks() - self.last_rotate_time))
        cooldown_percent = remaining_cooldown / self.COOLDOWN_TIME
        cooldown_bar_width = int(cooldown_percent * 100)
        pygame.draw.rect(screen, (255, 0, 0), (10, 10, cooldown_bar_width, 5))
