import pygame

class Car():
    def __init__(self, screen):
        """Initialize car and define car start position"""
        self.screen = screen
        self.image = pygame.image.load("images/car.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Draw car at this position"""
        self.screen.blit(self.image, self.rect)