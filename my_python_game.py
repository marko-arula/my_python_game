import pygame
from pygame.sprite import Group

from settings import Settings
from car import Car
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")

    car = Car(game_settings, screen)
    bullets = Group()

    alien = Alien(game_settings, screen)

    while True:
        gf.check_events(game_settings, screen, car, bullets)
        car.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, car, alien, bullets)

run_game()