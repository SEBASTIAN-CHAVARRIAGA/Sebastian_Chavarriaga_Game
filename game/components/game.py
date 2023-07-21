import pygame
import os
import game_over_menu

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE, HEART
from pygame.locals import QUIT, KEYDOWN, K_RETURN
from game.components.spaceship import Spaceship
from random import randint
from game.components.enemies.Enemy_Manager import EnemyManager
from game.components.Bullets.bullet_manager import BulletManager
from game.components.PowerUp.power_up_manager import PowerUpManager
from game.components.asteroids.asteroid import Asteroid
from game.components.asteroids.asteroid_manager import AsteroidManager
from game.components.Boss.boss import Boss
from game.components.Boss.boss_manager import BossManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.asteroid_manager = AsteroidManager()
        self.boss_manager = BossManager()
        self.player_bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.asteroid_group = pygame.sprite.Group()
        self.score = 0
        self.max_score = 0
        self.deaths_count = 0
        self.player_lives = 5 
        self.boss = None  
        self.spawn_boss = False


    def get_score(self):
        return self.score
    
    def draw_lives(self, screen):
        # Espaciado entre los íconos de vidas
        spacing = 30

        for i in range(self.player_lives):
            # Dibuja el ícono de vida en la posición correspondiente
            screen.blit(HEART, (10 + i * spacing, 30))

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.player.update(user_input, self.player_bullets)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.asteroid_manager.update(self)
        self.boss_manager.update(self)
        

              # Verifica si el jugador se quedó sin vidas
        if self.bullet_manager.player_lives <= 0:          
             # Muestra el menú de Game Over con la información relevante
            game_over_menu.game_over_screen(self.screen, self.score, self.max_score, self.deaths_count)
        
            # Limpia los elementos del juego antes de reiniciar
            self.player_bullets.empty()
            self.enemy_bullets.empty()
            self.enemy_manager.reset()
            self.bullet_manager.reset()
            self.player.reset()

            # Llama a una función separada para reiniciar el juego
            self.restart_game()

    def restart_game(self):
        # Vuelve a inicializar la instancia de Game
        new_game = Game()
        new_game.run()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.player_bullets.draw(self.screen)
        self.enemy_bullets.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.asteroid_manager.draw(self.screen)
        self.draw_lives(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()
      
            
    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show > 0:
                # Dibujar tiempo restante del power-up en la esquina superior izquierda
                font = pygame.font.Font(None, 24)
                text = font.render(f'{self.player.power_up_type} is enabled for {time_to_show} seconds', True, (0, 0, 0))
                self.screen.blit(text, (10, 10))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)