import sys

import pygame

from settings import  Settings 

def run_game():
    #Initialize pygame, settings,  and a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (85,223, 155 )
    # Start the main loop for the game.
    while True:
        #Watch for keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #Redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        #Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()

