import math

class Pheromone:
    def __init__(self, sid, x, y, intensity, speed):
        self.sid = sid
        self.x = x
        self.y = y
        self.intensity = float(intensity)
        self.radius = 1.0
        self.speed = float(speed)

    def tick(self, timedelta):
        self.radius += self.speed*timedelta

    def power(self):
        return self.intensity/self.radius

    def values_at(self, x, y):
        dist2 = (x-self.x)**2 + (y-self.y)**2
        val = math.exp(-dist2/(2*self.radius**2))
        return (val, val * (self.x-x)/self.radius**2, val * (self.y-y)/self.radius**2)