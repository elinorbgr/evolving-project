import pygame, random, sys, math
from pygame.locals import *



pygame.init()

size = 600
s=pygame.display.set_mode((size, size))
clock = pygame.time.Clock()

vel = 0.4
angv = 0.1
theta = 10

#Number of aniamls
nr = 5

#creates an animal image
img = pygame.Surface((20,20))

#initialises starting positions
xs = nr*[None]
ys = nr*[None]
for i in range(nr):
    xs[i] = random.randint(0,size)
    ys[i] = random.randint(0,size)

while True:
    clock.tick(10)
    deltatime = clock.get_time()
    
    #refresh page
    s.fill((255, 255, 255))
    
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit(0)
    #warp to opposite sides
    for i in range(0,nr):
        if xs[i] < 0:xs[i] = size
        if xs[i] > size:xs[i] = 0
        if ys[i] < 0:ys[i] = size
        if ys[i] > size:ys[i] = 0

        #Differential drive movement
        xs[i] += math.cos(theta)*vel*deltatime
        ys[i] += math.sin(theta)*vel*deltatime
        theta += angv*deltatime

        #display the image
        s.blit(img, (xs[i], ys[i]))

        pygame.display.update()
