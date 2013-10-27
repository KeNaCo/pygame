#!/bin/python3

import sys, pygame

if (__name__ == '__main__'): #main function
    pygame.init()
    
    size = width, heigh = 800, 450 #size of windows
    
    screen = pygame.display.set_mode(size)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()