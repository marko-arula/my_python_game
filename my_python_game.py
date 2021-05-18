import pygame
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

from car import Car
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Shooting car")
    # button to start the game
    play_button = Button(game_settings, screen, "Play")
    # game statistics object
    stats = GameStats(game_settings)
    # scoreboard of the game
    sb = Scoreboard(game_settings, screen, stats)


    car = Car(game_settings, screen)
    bullets = Group()

    aliens = Group()
    gf.create_fleet(game_settings, screen, car, aliens)

    while True:
        gf.check_events(game_settings, screen, stats, play_button, car, aliens, bullets)
        gf.update_screen(game_settings, screen, stats, sb, car, aliens, bullets, play_button)
        if stats.game_active == True:
            gf.update_bullets(game_settings, screen, stats, sb, car, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, car, aliens, bullets)
            car.update()


run_game()