import pygame
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats
from button import Button

from car import Car
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Example Game")
    # button to start the game
    play_button = Button(game_settings, screen, "Play")
    # game statistics object
    stats = GameStats(game_settings)

    car = Car(game_settings, screen)
    bullets = Group()

    aliens = Group()
    gf.create_fleet(game_settings, screen, car, aliens)

    while True:
        gf.check_events(game_settings, screen, car, bullets)
        car.update()
        gf.update_bullets(game_settings, screen, car, aliens, bullets)
        gf.update_aliens(game_settings, stats, screen, car, aliens, bullets)
        gf.update_screen(game_settings, screen, stats, car, aliens, bullets, play_button)

run_game()