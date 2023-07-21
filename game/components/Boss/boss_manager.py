import pygame
from game.components.Boss.boss import Boss
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class BossManager:
    def __init__(self):
        self.bosses = pygame.sprite.Group()
        self.spawned_boss = False  # Variable para controlar si el jefe ya ha sido creado

    def update(self, game):
        current_score = game.get_score()

        # Crea el jefe cuando el puntaje sea mayor a 100 y aún no haya aparecido
        if not self.spawned_boss and current_score >= 1000:
            boss = Boss(SCREEN_WIDTH, SCREEN_HEIGHT)  # las dimensiones de la pantalla
            self.bosses.add(boss)
            self.spawned_boss = True  # Marcar que el jefe ya ha sido creado

        # Actualizar todos los jefes
        self.bosses.update()

    def draw(self, screen):
        self.bosses.draw(screen)
