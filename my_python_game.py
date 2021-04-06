import sys
import pygame
from settings import Settings
from car import Car

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    car = Car(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(game_settings.bg_color)
        car.blitme()
        pygame.display.flip()
run_game()