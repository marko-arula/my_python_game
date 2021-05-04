import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, screen, car, bullets):
    """Check your keyboard events"""
    if event.key == pygame.K_RIGHT:
        car.moving_right = True
    if event.key == pygame.K_LEFT:
        car.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, car, bullets)
    if event.key == pygame.K_q:
        sys.exit()

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
            check_keydown_events(event, game_settings, screen, car, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, car)
                
def update_screen(game_settings, screen, car, aliens, bullets):
    # add screen background
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add car to screen
    car.blitme()
    # add alien to screen
    aliens.draw(screen)
    # display the last screen
    pygame.display.flip()

def update_bullets(game_settings, screen, car, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # Remove bullets and create new fleet
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(game_settings, screen, car, aliens)

def fire_bullet(game_settings, screen, car, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, car)
        bullets.add(new_bullet)

def get_number_aliens_x(game_settings, alien_width):
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, car_height, alien_height):
    available_space_y = game_settings.screen_height - 6 * alien_height - car_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, car, aliens):
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, car.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(game_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop_speed
    game_settings.fleet_direction *= -1

def update_aliens(game_settings, aliens):
    check_fleet_edges(game_settings, aliens)
    aliens.update()