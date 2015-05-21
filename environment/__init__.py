import math

def distance(x, y, a, b):
    return math.sqrt((x-a)**2 + (y-b)**2)

class Food:
    def __init__(self, x, y, amount):
        self.x = x
        self.y = y
        self.amount = amount

    def update(self, animals):
        for a in animals:
            if distance(a.x, a.y, self.x, self.y) < 8:
                consume = min(self.amount, 100 - a.energy)
                self.amount -= consume
                a.energy += consume
                if self.amount <= 0:
                    break

    def smell_at(self, x, y):
        val = 1 / distance(self.x, self.y, x, y)
        gradx = -2 * (x - self.x) * (val**2)
        grady = -2 * (y - self.y) * (val**2)
        return (val, gradx, grady)