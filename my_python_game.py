import pygame
from pygame.sprite import Group

from settings import Settings
from car import Car
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    car = Car(game_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(game_settings, screen, car, bullets)
        car.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, car, bullets)

run_game()