import math

from environment import Pheromone, distance
from conf import PREDATOR_SPEED

class Predator:
    kind = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tick = 1.0


    def update(self, animals, pheromones, timedelta, width, height):
        (tx, ty) = (0,0)
        nearest = width + height

        for a in animals:
            x = a.x
            y = a.y
            # take the warping into account
            if x - self.x > width / 2:
                x -= width
            elif x - self.x < -width / 2:
                x += width
            if y - self.y > height / 2:
                y -= height
            elif y - self.y < -height / 2:
                y += height
            dist = distance(x, y, self.x, self.y)
            if dist < 12:
                a.energy = -100
            elif dist < nearest:
                nearest = dist
                (tx, ty) = (x, y)

        dir_x = tx - self.x
        dir_y = ty - self.y
        norm = math.sqrt(dir_x**2 + dir_y**2)
        self.x += dir_x * PREDATOR_SPEED * timedelta / norm
        self.y += dir_y * PREDATOR_SPEED * timedelta / norm

        if self.x > width: self.x -= width
        if self.x < 0: self.x += width
        if self.y > height: self.y -= height
        if self.y < 0: self.y += height

        self.tick -= timedelta
        if self.tick <= 0:
            self.tick = 1.0
            pheromones.append(Pheromone(self.kind, self.x, self.y, 15, PREDATOR_SPEED*1.5))

