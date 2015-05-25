import math, random

from animal import Animal
from environment import Food

PHEROMONES = 2

ANIMALS_BASE_SPEED = 50
ANIMALS_BASE_ANGULAR_SPEED = 5

class Simulator:
    def __init__(self, space_width, space_height, animal_count, genomes):
        self.width = space_width
        self.height = space_height
        self.genomes = genomes
        self.animals = [ Animal(random.choice(genomes), PHEROMONES) for _ in range(animal_count) ]
        self.foods = [
            Food(
                random.randrange(0, self.width, 1),
                random.randrange(0, self.height, 1),
                10
            ) for _ in range(animal_count)
        ]
        for a in self.animals:
            a.teleport(
                random.randrange(0, self.width, 1),
                random.randrange(0, self.height, 1),
                random.uniform(0, 6.28)
            )
        self.food_frequency = 1.0
        self.next_food = 1.0
        self.pheromones = []

    def update(self, timestep):
        self.next_food -= timestep
        if self.next_food <= 0.0:
            self.next_food = self.food_frequency
            self.foods.append(Food(
                random.randrange(0, self.width, 1),
                random.randrange(0, self.height, 1),
                10
            ))

        for a in self.animals:
            # compute food smells
            val = [0.0 for _ in range(PHEROMONES)]
            gradx = [0.0 for _ in range(PHEROMONES)]
            grady = [0.0 for _ in range(PHEROMONES)]
            for f in self.pheromones:
                x = a.x
                y = a.y
                # take the warping into account
                if x - f.x > self.width / 2:
                    x -= self.width
                elif x - f.x < -self.width / 2:
                    x += self.width
                if y - f.y > self.height / 2:
                    y -= self.height
                elif y - f.y < -self.height / 2:
                    y += self.height
                (fval, fgx, fgy) = f.values_at(x, y)
                val[f.sid] += fval
                gradx[f.sid] += fgx
                grady[f.sid] += fgy
            angle_val = [
                math.tanh(math.tan((math.atan2(gy, gx) - a.theta)/2)) for (gy, gx) in zip(grady, gradx)
            ]
            # update animals
            a.update(zip(val, angle_val), timestep, ANIMALS_BASE_SPEED, ANIMALS_BASE_ANGULAR_SPEED, self.pheromones)
            if a.x > self.width: a.x -= self.width
            if a.x < 0: a.x += self.width
            if a.y > self.height: a.y -= self.height
            if a.y < 0: a.y += self.height

        for f in self.foods:
            f.update(self.animals, self.pheromones, timestep)

        for f in self.pheromones:
            f.tick(timestep)

        # kill dead animals
        self.animals = [ a for a in self.animals if a.energy > 0.0 ]
        # remove finished foods
        self.foods = [ f for f in self.foods if f.amount > 0.0 ]
        # remove vanished pheromones
        self.pheromones = [ f for f in self.pheromones if f.power() > 0.1 ]