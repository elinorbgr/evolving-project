import math

from conf import INITIAL_ENERGY

class Predator:

    theta = 0
    x = 0
    y = 0
    p_cooldown = 0.0

    def __init__(self):
        self.energy = 100

    def update(self):

        # pheromones
        new_pheromones = []
        if self.p_cooldown <= 0:
            for (i,v)in enumerate(outputs):
                if v > 0:
                    new_pheromones.append(Pheromone(i, self.x, self.y, v*10, 10))
            self.p_cooldown = 1.0
        else:
            self.p_cooldown -= deltatime
        return new_pheromones
    
    def teleport(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta


