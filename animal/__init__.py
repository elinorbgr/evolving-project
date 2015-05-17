from neural.brain import Brain

class AnimalOutput:
    def __init__(self, speed, angular_speed, outputs):
        self.speed = speed
        self.angular_speed = angular_speed
        self.outputs = outputs

class Animal:
    def __init__(self, genome):
        self.brain = Brain(genome, ["Ea"], ["Mx", "My"])
        self.energy = 50.0

    def update(self, inputs):
        (hard_out, outputs) = self.brain.compute({ "Ea": self.energy }, inputs)
        speed = hard_out["Mx"]
        angular_speed = hard_out["My"]
        self.energy -= 0.01 + 0.1 * speed
        return AnimalOutput(speed, angular_speed, outputs)