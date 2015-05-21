import random

from animal import Animal

PHEROMONES = 8

class Simulator:
    def __init__(self, space_width, space_height, animal_count, genomes):
        self.width = space_width
        self.height = space_height
        self.genomes = genomes
        self.animals = [ Animal(random.choice(genomes), PHEROMONES) for _ in range(animal_count) ]
        for a in self.animals:
            a.teleport(
                random.randrange(0, self.width, 1),
                random.randrange(0, self.height, 1),
                random.uniform(0, 6.28)
            )

    def update(self, timestep):
        for a in self.animals:
            # two last arguments are:
            # - max speed in pixels per second
            # - max angular speed in radian per second
            a.update([], timestep, 50, 5)
            if a.x > self.width: a.x -= self.width
            if a.x < 0: a.x += self.width
            if a.y > self.height: a.y -= self.height
            if a.y < 0: a.y += self.height
        # kill dead animals
        self.animals = [ a for a in self.animals if a.energy > 0.0 ]