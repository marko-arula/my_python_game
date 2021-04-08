import sys
import pygame
from bullet import Bullet
def check_keydown_events(event, car):
    """Check your keyboard events"""
    if event.key == pygame.K_RIGHT:
        car.moving_right = True
    if event.key == pygame.K_LEFT:
        car.moving_left = True
def check_keyup_events(event, car):
    """Check your keyboard events"""
    if event.key == pygame.K_RIGHT:
        car.moving_right = False
    if event.key == pygame.K_LEFT:
        car.moving_left = False
def check_events(game_settings, screen, car, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                car.moving_right = True
            if event.key == pygame.K_LEFT:
                car.moving_left = True
            if event.key == pygame.K_UP:
                car.moving_up = True
            if event.key == pygame.K_DOWN:
                car.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                car.moving_right = False
            if event.key == pygame.K_LEFT:
                car.moving_left = False
            if event.key == pygame.K_UP:
                car.moving_up = False
            if event.key == pygame.K_DOWN:
                car.moving_down = False
                
def update_screen(game_settings, screen, car, bullets):
    # add screen background
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add car to screen
    car.blitme()
    # display the last screen
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(game_settings, screen, car, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, car)
        bullets.add(new_bullet)