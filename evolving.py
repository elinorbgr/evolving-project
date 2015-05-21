#!/bin/env python2

import pygame, random, sys, math
from pygame.locals import *

from simulator import Simulator

def main():
    # init phase
    (width, heigth) = (800, 600)

    pygame.init()
    s = pygame.display.set_mode((width, heigth))
    clock = pygame.time.Clock()
    s.fill((255,255,255))

    # genomes = ["+5A00i-1A000iMx", "+5A00i-1A000iMx-5A00iMy", "+5A00i-1A000iMx-Ai5M00y"]
    genomes = ["+5A00i-1A000iMx+Fd-10F00dMy"]

    sim = Simulator(width, heigth, 30, genomes)

    while True:
        deltatime = float(clock.tick(50)) / 1000
        s.fill((255, 255, 255))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)

        sim.update(deltatime)

        # display the food
        fcol = pygame.Color(0,0,255)
        for f in sim.foods:
            pygame.draw.circle(s, fcol, (f.x, f.y), 5)

        # display the animals
        for a in sim.animals:
            # choose a color:
            col = pygame.Color(int((100-a.energy)*255/100), int(a.energy*255/100), 0, 255)
            # draw a body
            pygame.draw.circle(s, col, (int(a.x), int(a.y)), 8)
            # draw a head
            pygame.draw.circle(s, col, (int(a.x + math.cos(a.theta)*7), int(a.y + math.sin(a.theta)*7)), 5)

        pygame.display.update()


if __name__ == '__main__':
    main()
