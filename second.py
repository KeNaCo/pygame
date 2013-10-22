#!/bin/python3

import sys, pygame

if (__name__ == '__main__'): #main function
    pygame.init()
    
    size = width, heigh = 800, 450
    
    screen = pygame.display.set_mode(size)
    
    picture = pygame.image.load("tux_samurai.bmp")
    
    screen.blit(picture, (200,100))
    screen.blit(picture, (0,0))
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()