import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, game_setting, screen, car):
        super().__init__()
        self.screen = screen
        # create bullet
        self.rect = pygame.Rect(0, 0, game_setting.bullet_width, game_setting.bullet_height)
        self.rect.centerx = car.rect.centerx
        self.rect.top = car.rect.top
        self.y = float(self.rect.y)
        # bullet settings
        self.color = game_setting.bullet_color
        self.speed_factor = game_setting.bullet_speed_factor
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)