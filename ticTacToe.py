import pygame
import sys
def main:
    pygame.init()

    size = width, height = 400, 400
    screen = pygame.display.set_mode(size)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
