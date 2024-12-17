#
#  1. Rain 

import time, pygame
from random import randint

WIDTH, HEIGHT = 1000, 500

pink = (255,153,255)
purple = (153,0,153)

class Drop():
    def __init__(self,x,y,v,color ) -> None:
        self.x = x
        self.y = y
        self.v = v
        self.color = color
            
    def move_drop(self):
        self.y = self.y + self.v
        if self.y > HEIGHT:
            self.y = randint(-100,-50)
            self.x = randint(0,WIDTH)
            self.v = randint(1,4)


class Rain():
    def __init__(self, intensity):
        self.intensity = intensity
        self.drops = []
        for i in range(self.intensity):
            self.drops.append(Drop(randint(0,WIDTH), randint(-100,-50),  randint(1,4), purple))
        
    def fall(self):
        for i in range(len(self.drops)):
            self.drops[i].move_drop()
        
rain = Rain(300)

pygame.init()

win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Rainning !")

running = True    
while running:

    win.fill(pink)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False

    for i in range(rain.intensity):
        pygame.draw.rect(win,rain.drops[i].color,(rain.drops[i].x,rain.drops[i].y,rain.drops[i].v,6*rain.drops[i].v))
    
    
    rain.fall()
    time.sleep(0.005)

    pygame.display.update()

pygame.quit()