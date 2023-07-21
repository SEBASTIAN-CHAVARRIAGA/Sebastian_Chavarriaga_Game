import pygame
import os


# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

AURA = pygame.image.load(os.path.join(IMG_DIR, "Other/power_blue.png"))
AURA_WIDTH = 80  
AURA_HEIGHT = 80

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

BOSS = pygame.image.load(os.path.join(IMG_DIR, "bossI/final-boss.gif"))

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

ASTEROID_1 = pygame.image.load(os.path.join(IMG_DIR, "Asteroids/asteroid1.png"))
ASTEROID_1 = pygame.transform.scale(ASTEROID_1, (100, 100))

ASTEROID_2 = pygame.image.load(os.path.join(IMG_DIR, "Asteroids/asteroid2.png"))
ASTEROID_2 = pygame.transform.scale(ASTEROID_2, (100, 100))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

SHIP_WIDTH = 40
SHIP_HEIGHT = 60

FONT_STYLE = 'freesansbold.ttf'

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)