import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, game_settings, screen, car, bullets):
    """Check your keyboard events"""
    if event.key == pygame.K_RIGHT:
        car.moving_right = True
    if event.key == pygame.K_LEFT:
        car.moving_left = True
    if event.key == pygame.K_DOWN:
        car.moving_down = True
    if event.key == pygame.K_UP:
        car.moving_up = True
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
    if event.key == pygame.K_DOWN:
        car.moving_down = False
    if event.key == pygame.K_UP:
        car.moving_up = False

def check_events(game_settings, screen, stats, play_button, car, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, car, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, car)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats, play_button, car, aliens, bullets, mouse_x, mouse_y)

def check_play_button(game_settings, screen, stats, play_button, car, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        game_settings.init_dynamic_scale()
        stats.game_active = True
        pygame.mouse.set_visible(False)
        aliens.empty()
        bullets.empty()
        create_fleet(game_settings, screen, car, aliens)
        car.car_center()

def update_screen(game_settings, screen, stats, sb, car, aliens, bullets, play_button):
    # add screen background
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add car to screen
    car.blitme()
    # add alien to screen
    aliens.draw(screen)
    # show scoreboard
    sb.draw_score()
    # display play button
    if stats.game_active == False:
        play_button.draw_button()
    # display the last screen
    pygame.display.flip()

def update_bullets(game_settings, screen, stats, sb, car, aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(game_settings, screen, stats, sb, car, aliens, bullets)
    
def check_bullet_alien_collisions(game_settings, screen, stats, sb, car, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        stats.score += game_settings.alien_points
        sb.prepare_score()
    # Remove bullets and create new fleet
    if len(aliens) == 0:
        bullets.empty()
        game_settings.increase_speed()
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

def update_aliens(game_settings, stats, screen, car, aliens, bullets):
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    # Check collisions between car and aliens
    if pygame.sprite.spritecollideany(car, aliens):
        car_hit(game_settings, stats, screen, car, aliens, bullets)
    # check aliens appear screen bottom
    check_aliens_bottom(game_settings, stats, screen, car, aliens, bullets)


def car_hit(game_settings, stats, screen, car, aliens, bullets):
    if stats.cars_left > 0:
        # cars left minus 1
        stats.cars_left = stats.cars_left - 1
        # aliens and bullets groups are empty
        aliens.empty()
        bullets.empty()
        # creates an aliens fleet
        create_fleet(game_settings, screen, car, aliens)
        # center car
        car.car_center()
        # pause
        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(game_settings, stats, screen, car, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            car_hit(game_settings, stats, screen, car, aliens, bullets)
            break