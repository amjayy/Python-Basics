import pygame
background = pygame.image.load( "ship.bmp") #this is our backrpund image

import pygame

from settings import Settings
from ship import Ship

import game_functions as gf


def run_game():
    #Initialize pygame,settings, and screen objects.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
           ( ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #Set background color
    bg_color =(230, 230, 230)
    #Make a ship
    ships = Ship(ai_settings, screen)
    

    # Start the main loop for the game.
    while True:
            gf.check_events(ship)
            ship.update()
            gf.update_screen(ai_settings, screen, ship)
            screen.fill(ai_settings.bg_color)
run_game()
