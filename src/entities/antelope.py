from .animal import Animal
import random

class Antelope(Animal):
    color = (140, 70, 0)
    symbol = 'AT'

    def __init__(self, world, position):
        super().__init__(world, position, 4, 4)

    def __str__(self):
        return 'Antelope'

    def action(self):
        v_or_h = random.randint(0, 1)
        n_or_p = random.randint(0, 1)

        if v_or_h == 1:
            self.move(0, -2 if n_or_p == 1 else 2)
        else:
            self.move(-2 if n_or_p == 2 else 1, 0)

    def collision(self, other):
        if (random.randint(0, 1) == 1):
            super().collision(other)
        else:
            free = self.world.getFreeSpaceAround(self.position)
            count = len(free)
            if count > 0:
                d = free[random.randint(0, count - 1)]
                self.move(d[0] - self.position[0], d[1] - self.position[1])
            else:
                super().collision(other)

    def getColor(self):
        return Antelope.color

    def getSymbol(self):
        return Antelope.symbol
