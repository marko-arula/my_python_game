import pygame

class Car():
    def __init__(self, game_settings, screen):
        """Initialize car and define car start position"""
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("images/car.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update car position according to moving flag"""
        if self.moving_right:
            self.center += self.game_settings.car_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.car_speed_factor
        self.rect.centerx = self.center
    def blitme(self):
        """Draw car at this position"""
        self.screen.blit(self.image, self.rect)