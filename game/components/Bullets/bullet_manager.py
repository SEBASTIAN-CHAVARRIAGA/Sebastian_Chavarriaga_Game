import pygame

from game.utils.constants import SCREEN_HEIGHT
class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.player_lives = 5  # Agregamos esta variable para llevar el control de las vidas del jugador

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != 'enemy':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score += 10 
            
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
             if not game.player.has_power_up:
                self.enemy_bullets.remove(bullet)
                self.player_lives -= 1  # Restamos una vida al jugador cuando recibe una bala enemiga
                if self.player_lives <= 0:
                    game.deaths_count += 1 
                    game.playing = False
                    pygame.time.delay(1000)
                    break

    def draw(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 5:  
            self.enemy_bullets.append(bullet)

    def reset(self):
        self.bullets.clear()