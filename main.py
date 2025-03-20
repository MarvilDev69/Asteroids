# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    number = 5 
    while number !=0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        number -= 2

    pygame.display.set_palette(1,1,1)
    pygame.display.flip()
    #print("Starting Asteroids!")
    #print("Screen width:", SCREEN_WIDTH)
    #print("Screen height:",SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
