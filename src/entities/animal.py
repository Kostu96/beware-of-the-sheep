from .entity import Entity
from .plant import Plant
import random

class Animal(Entity):
    def __init__(self, world, position, strength, initiative):
        super().__init__(world, position, strength, initiative)

    def action(self):
        v_or_h = random.randint(0, 1)
        n_or_p = random.randint(0, 1)

        if v_or_h == 1:
            self.move(0, -1 if n_or_p == 1 else 1)
        else:
            self.move(-1 if n_or_p == 1 else 1, 0)

    def collision(self, other):
        if isinstance(other, Plant):
            other.kill()
            self.world.addMessage(str(other) + ' was eaten by ' + str(self))
            other.collision(self)
        elif isinstance(other, self.__class__):
            self.moveToPrevPosition()
            free = self.world.getFreeSpaceAround(self.position)
            count = len(free)
            if count > 0:
                self.world.spawnEntity(self, free[random.randint(0, count - 1)])
        elif other.dodgedAttack(self.strength):
            self.moveToPrevPosition()
        elif other.strength <= self.strength:
            other.kill()
            self.world.addMessage(str(other) + ' was slain by ' + str(self))
        else:
            self.kill()
            self.world.addMessage(str(self) + ' was slain by ' + str(other))
