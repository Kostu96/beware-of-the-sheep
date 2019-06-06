from .entity import Entity
import random

class Plant(Entity):
    def __init__(self, world, position, strength):
        super().__init__(world, position, strength, 0)

    def action(self):
        if random.randint(0, 7) == 0:
            free = self.world.getFreeSpaceAround(self.position)
            count = len(free)
            if count > 0:
                self.world.spawnEntity(self, free[random.randint(0, count - 1)])

    def collision(self, other):
        pass
