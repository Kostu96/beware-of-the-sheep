from .animal import Animal
import random

class Fox(Animal):
    color = (225, 97, 10)
    symbol = 'FX'

    def __init__(self, world, position):
        super().__init__(world, position, 3, 7)

    def __str__(self):
        return 'Fox'

    def action(self):
        dirs = []
        pos = self.position
        positions = [
            (pos[0], self.position[1] - 1 if pos[1] > 0 else self.height - 1),
            (pos[0], (pos[1] + 1) % self.height),
            (pos[0] - 1 if pos[0] > 0 else self.width - 1, pos[1]),
            ((pos[0] + 1) % self.width, pos[1])
        ]
        for p in positions:
            e = self.world.getEntityAt(self, p)
            if not e or e.strength <= self.strength:
                dirs.append(p)

        p = dirs[random.randint(0, len(dirs) - 1)]
        self.move(p[0] - pos[0], p[1] - pos[1])

    def getColor(self):
        return Fox.color

    def getSymbol(self):
        return Fox.symbol

