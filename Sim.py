import pygame, random, sys
from pygame.locals import *


size = 600
pygame.init()
s=pygame.display.set_mode((size, size))
s.fill((255,255,255))

nr = 5

img = pygame.Surface((20,20))
xs = nr*[None]
ys = nr*[None]
dirs = nr*[None]
for i in range(nr):
    dirs[i] = random.randint(0,3)
    xs[i] = random.randint(0,size)
    ys[i] = random.randint(0,size)

print(dirs)
print(xs)
print(ys)
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
    s.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)

    for i in range(0,nr):
        if xs[i] < 0:xs[i] = size
        if xs[i] > size:xs[i] = 0
        if ys[i] < 0:ys[i] = size
        if ys[i] > size:ys[i] = 0

        dirs[i] = turn(dirs[i])
        
        if dirs[i]==0:ys[i] += 20;
        elif dirs[i]==1:xs[i] += 20
        elif dirs[i]==2:ys[i] -= 20
        elif dirs[i]==3:xs[i] -= 20

        
        s.blit(img, (xs[i], ys[i]))

        
        
        pygame.display.update()
