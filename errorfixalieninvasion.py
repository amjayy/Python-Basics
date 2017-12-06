import pygame

import sys

def run_game():
    #Intialize the game to create a screen object.
    pygame.init()
    screen= pygame.display.set_mode((1200, 800 ))
    pygame.display.set_caption("Alien Invasion")

    #Start the main game loop for the game.
    while True:
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
             sys.exit()
