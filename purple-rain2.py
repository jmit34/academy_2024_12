#
#  1. Multiple Drops 

import time, pygame
from random import randint


WIDTH, HEIGHT = 800, 800

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
            self.v = randint(2,5)

drop = Drop(randint(0,WIDTH),randint(-100,-50),randint(2,5),purple)

drop2 = Drop(randint(0,WIDTH),randint(-100,-50),randint(2,5),purple)

drop3 = Drop(randint(0,WIDTH),randint(-100,-50),randint(2,5),purple)


pygame.init()

win = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Purple Rain Multiple Drops")


running = True
    
while running:

    win.fill(pink)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_q:
                running = False

    
    pygame.draw.rect(win,drop.color,(drop.x,drop.y,drop.v,6*drop.v))
    pygame.draw.rect(win,drop2.color,(drop2.x,drop2.y,drop2.v,6*drop2.v))
    pygame.draw.rect(win,drop3.color,(drop3.x,drop3.y,drop3.v,6*drop3.v))


 
    drop.move_drop()
    drop2.move_drop()
    drop3.move_drop()
    time.sleep(0.01)

    pygame.display.update()

pygame.quit()