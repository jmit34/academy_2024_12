#
#  1. Single drop is falling down 

import time, pygame
from random import randint


WIDTH, HEIGHT = 800, 800

pink = (255,153,255)
purple = (153,0,153)

pygame.init()

win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Purple Rain Single Drop")

x = randint(1,WIDTH)
y = randint(-100,-50)
v = randint(2,6)

running = True

while running:

    win.fill(pink)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False

    pygame.draw.rect(win,purple,(x,y,v,6*v))
    y = y + v


    time.sleep(0.01)

    pygame.display.update()

pygame.quit()