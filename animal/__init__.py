import math

from neural.brain import Brain

from environment.pheromone import Pheromone

from conf import LIFE_COST, MOVE_COST

ENERGY_NEURON = "La"
SPEED_NEURON = "Mx"
ANGSPEED_NEURON = "Nx"

class Animal:

    theta = 0
    x = 0
    y = 0
    p_cooldown = 0.0

    def __init__(self, genome, pheromone_count):
        self.brain = Brain(genome, [ENERGY_NEURON], [SPEED_NEURON, ANGSPEED_NEURON], pheromone_count)
        self.energy = 50.0

    def update(self, inputs, deltatime, v_scale, angv_scale, pheromones):
        (hard_out, outputs) = self.brain.compute({ ENERGY_NEURON: self.energy }, inputs)
        speed = hard_out[SPEED_NEURON]
        angular_speed = hard_out[ANGSPEED_NEURON]
        self.energy -= (LIFE_COST + MOVE_COST * speed) * deltatime
        self.x += math.cos(self.theta) * speed * deltatime * v_scale
        self.y += math.sin(self.theta) * speed * deltatime * v_scale
        self.theta += angular_speed * deltatime * angv_scale
        if self.theta > 2*math.pi:
            self.theta -= 2*math.pi
        elif self.theta < 0:
            self.theta += 2*math.pi
        # pheromones
        if self.p_cooldown <= 0:
            for (i,v)in enumerate(outputs):
                if v > 0.5:
                    pheromones.append(Pheromone(i, self.x, self.y, v*10, 10))
            self.p_cooldown = 1.0
        else:
            self.p_cooldown -= deltatime

    def teleport(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta
