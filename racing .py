import pygame
import sys
import time
import random


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Py Racer")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    pygame.display.flip()

run_game()
