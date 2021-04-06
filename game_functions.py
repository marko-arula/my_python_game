import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(game_settings, screen, car):
    # add screen background
    screen.fill(game_settings.bg_color)
    # add car to screen
    car.blitme()
    # display the last screen
    pygame.display.flip()