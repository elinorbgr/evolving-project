import pygame, random, sys
from pygame.locals import *

# start point
xs = 300
ys = 300

size = 600

pygame.init()
s=pygame.display.set_mode((size, size))
s.fill((255,255,255))


img = pygame.Surface((20, 20))
dirs = 0
clock = pygame.time.Clock()

def turn(cur):
    turn = random.randint(0,100)
    prob = random.randint(0,100)
    nex = cur
    if prob > 50:
        if turn < 25 and cur == 0:nex = 1
        elif turn > 75 and cur == 0:nex = 3
        elif turn < 25 and cur == 1:nex = 2
        elif turn > 75 and cur == 1:nex = 0
        elif turn < 25 and cur == 2:nex = 1
        elif turn > 75 and cur == 2:nex = 3
        elif turn < 25 and cur == 3:nex = 0
        elif turn > 75 and cur == 3:nex = 2
    return nex
    
    

while True:
    clock.tick(10)

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
    dirs = turn(dirs)
    if xs < 0:xs = size
    if xs > size:xs = 0
    if ys < 0:ys = size
    if ys > size:ys = 0
    if dirs==0:ys += 20;
    elif dirs==1:xs += 20
    elif dirs==2:ys -= 20
    elif dirs==3:xs -= 20

	
    s.fill((255, 255, 255))	
    s.blit(img, (xs, ys));pygame.display.update()
