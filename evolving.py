#!/bin/env python2

import pygame, random, sys, math
from pygame.locals import *

from animal import Animal

def main():
    # init phase
    size = 600
    pygame.init()
    s = pygame.display.set_mode((size, size))
    clock = pygame.time.Clock()
    s.fill((255,255,255))

    nb_animals = 30

    genomes = ["+5A00i-1A000iMx", "+5A00i-1A000iMx-5A00iMy", "+5A00i-1A000iMx-Ai5M00y"]

    animals = [ Animal(random.choice(genomes)) for _ in range(nb_animals) ]
    for a in animals:
        a.teleport(
            random.randrange(0, 600, 1),
            random.randrange(0, 600, 1),
            random.uniform(0, 6.28)
        )

    while True:
        deltatime = float(clock.tick(50)) / 1000
        s.fill((255, 255, 255))
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)

        for a in animals:
            # two last arguments are:
            # - max speed in pixels per second
            # - max angular speed in radian per second
            a.update({}, deltatime, 50, 5)
            if a.x > size: a.x -= size
            if a.x < 0: a.x += size
            if a.y > size: a.y -= size
            if a.y < 0: a.y += size
            # draw a body
            pygame.draw.circle(s, 0, (int(a.x), int(a.y)), 8)
            # draw a head
            pygame.draw.circle(s, 0, (int(a.x + math.cos(a.theta)*7), int(a.y + math.sin(a.theta)*7)), 5)

        pygame.display.update()


if __name__ == '__main__':
    main()