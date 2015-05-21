import math

from neural.brain import Brain

class Animal:

    theta = 0
    x = 0
    y = 0

    def __init__(self, genome, pheromone_count):
        self.brain = Brain(genome, ["Ea"], ["Mx", "My"], pheromone_count)
        self.energy = 50.0

    def update(self, inputs, deltatime, v_scale, angv_scale):
        (hard_out, outputs) = self.brain.compute({ "Ea": self.energy }, inputs)
        speed = hard_out["Mx"]
        angular_speed = hard_out["My"]
        self.energy -= 0.01 + 0.1 * speed * deltatime
        self.x += math.cos(self.theta) * speed * deltatime * v_scale
        self.y += math.sin(self.theta) * speed * deltatime * v_scale
        self.theta += angular_speed * deltatime * angv_scale
        if self.theta > 2*math.pi:
            self.theta -= 1*math.pi
        elif self.theta < 0:
            self.theta += 2*math.pi
        return outputs

    def teleport(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta