import pygame 
from pygame.sprite import Sprite
from random import randint, choice

from game.components.enemies.enemy import Enemy, Enemy2

class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()
        
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 5:
            if randint(1, 10) <= 7:
                enemy = Enemy()
            else:
                enemy = Enemy2()
            self.enemies.append(enemy)
