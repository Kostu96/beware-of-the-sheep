from .entities import Animal
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


class CyberSheep(Animal):
    color = (184, 3, 255)
    symbol = 'CS'

    def __init__(self, world, position):
        super().__init__(world, position, 11, 4)

    def __str__(self):
        return 'Cyber Sheep'

    def action(self):
        pos = self.world.getClosestHogweed(self.position)
        if pos == (-1, -1):
            return

        d1x = self.position[0] - pos[0]
        d2x = pos[0] + (self.world.width - self.position[0])
        d1y = self.position[1] - pos[1]
        d2y = pos[1] + (self.world.height - self.position[1])
        dx = abs(d1x if abs(d1x) < abs(d2x) else d2x)
        dy = abs(d1y if abs(d1y) < abs(d2y) else d2y)
        if dx > dy:
            if abs(d1x) < abs(d2x):
                self.move(-1, 0)
            else:
                self.move(1, 0)
        else:
            if abs(d1y) < abs(d2y):
                self.move(0, -1)
            else:
                self.move(0, 1)

    def getColor(self):
        return CyberSheep.color

    def getSymbol(self):
        return CyberSheep.symbol


class Fox(Animal):
    color = (225, 97, 10)
    symbol = 'FX'

    def __init__(self, world, position):
        super().__init__(world, position, 3, 7)

    def __str__(self):
        return 'Fox'

    def action(self):
        pass

    def getColor(self):
        return Fox.color

    def getSymbol(self):
        return Fox.symbol


class Human(Animal):
    color = (250, 200, 250)
    symbol = 'HM'

    def __init__(self, world, position):
        super().__init__(world, position, 5, 4)

    def __str__(self):
        return 'Human'

    def getColor(self):
        return Human.color

    def getSymbol(self):
        return Human.symbol


class Sheep(Animal):
    color = (250, 250, 250)
    symbol = 'SH'

    def __init__(self, world, position):
        super().__init__(world, position, 4, 4)

    def __str__(self):
        return 'Sheep'

    def getColor(self):
        return Sheep.color

    def getSymbol(self):
        return Sheep.symbol


class Turtle(Animal):
    color = (30, 90, 30)
    symbol = 'TT'

    def __init__(self, world, position):
        super().__init__(world, position, 2, 1)

    def __str__(self):
        return 'Turtle'

    def getColor(self):
        return Turtle.color

    def getSymbol(self):
        return Turtle.symbol


class Wolf(Animal):
    color = (100, 110, 110)
    symbol = 'WF'

    def __init__(self, world, position):
        super().__init__(world, position, 9, 5)

    def __str__(self):
        return 'Wolf'

    def getColor(self):
        return Wolf.color

    def getSymbol(self):
        return Wolf.symbol
