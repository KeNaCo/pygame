#!/bin/python3

import sys, pygame
state_x = 0
state_y = 0

def chColor(r):
    r += 1
    if r >= 255:
        r = 0
    
    return r

def animate(x, y):
    global state_x, state_y
    if (state_x == 0):
        x += 1
        if (x + 300) > 800:
            state_x = 1
    elif state_x == 1:
        x -= 1
        if x < 0:
            state_x = 0
    
    if state_y == 0:
        y += 1
        if (y + 300) > 450:
            state_y = 1
    elif state_y == 1:
        y -= 1
        if y < 0:
            state_y = 0
#    print("x, y: ", x , y)
    return (x,y)

if (__name__ == '__main__'): #main function
    pygame.init()
    
    #setting window size
    size = width, heigh = 800, 450
    screen = pygame.display.set_mode(size)
    
    #loading picture
    picture = pygame.image.load("tux_samurai.bmp")
    
    #picture position
    x = y = 0
    r = 0x6f
    
    #main render loop
    while True:
        #looking for end event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
        
        r = chColor(r)
        screen.fill((r,0xdc,0x47))
        screen.blit(picture, (x,y))
        pygame.display.flip()
        x, y = animate(x, y)