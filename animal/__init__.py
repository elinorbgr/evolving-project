
class AnimalOutput:
    speed = 0.0
    angular_speed = 0.0

    def __init__(self, speed, angular_speed):
        self.speed = speed
        self.angular_speed = angular_speed

class Animal:
    def __init__(self, genom):
        pass

    def update(self, inputs):
        return AnimalOutput(0.0, 0.0)