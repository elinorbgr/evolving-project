#!/bin/env python3

import pygame, random, sys, math
from pygame.locals import *

from neural import random_genome
from simulator import Simulator

from conf import WIDTH, HEIGHT, ANIMAL_COUNT, TIME_TICK
from conf import INIT_GENOME_LEN, INIT_GENOME_POOL

PHEROMONES_COLORS = [
    (0,0,255),
    (255,0,0),
    (0,255,0),
    (0,0,0)
]

def main():
    # init phase

    pygame.init()
    s = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    s.fill((255,255,255))

    #genomes = ["+133M10l-33M220lMx+Ld-33L220dNx"]

    genomes = [ random_genome(INIT_GENOME_LEN) for _ in range(INIT_GENOME_POOL) ]

    sim = Simulator(WIDTH, HEIGHT, ANIMAL_COUNT, genomes)

    while True:
        deltatime = float(clock.tick(50)) / 1000
        deltatime = TIME_TICK
        s.fill((255, 255, 255))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)

        sim.update(deltatime)

        # display the pheromones
        for p in sim.pheromones:
            i = min(p.power(), 1.0)
            (r,g,b) = PHEROMONES_COLORS[p.sid]
            col = (int(255*(1.0-i) + r*i),int(255*(1.0-i) + g*i),int(255*(1.0-i) + b*i), 255)
            pygame.draw.circle(s, col, (int(p.x), int(p.y)), int(p.radius), 1)

        # display the objects
        for f in sim.objects:
            pygame.draw.circle(s, PHEROMONES_COLORS[f.kind], (f.x, f.y), 5)
            pygame.draw.circle(s, (0,0,0), (f.x, f.y), 5, 1)

        # display the animals
        for a in sim.animals:
            # choose a color:
            col = pygame.Color(int((100-a.energy)*255/100), int(a.energy*255/100), 0, 255)
            # draw a head
            pygame.draw.circle(s, col, (int(a.x + math.cos(a.theta)*7), int(a.y + math.sin(a.theta)*7)), 5)
            pygame.draw.circle(s, (0,0,0), (int(a.x + math.cos(a.theta)*7), int(a.y + math.sin(a.theta)*7)), 5, 1)
            # draw a body
            pygame.draw.circle(s, col, (int(a.x), int(a.y)), 8)
            pygame.draw.circle(s, (0,0,0), (int(a.x), int(a.y)), 8, 1)

        pygame.display.update()


if __name__ == '__main__':
    main()
