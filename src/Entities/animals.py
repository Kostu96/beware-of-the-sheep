from .entities import Animal


class Antelope(Animal):
    color = (140, 70, 0)
    symbol = 'AT'

    def __init__(self, world, position):
        super().__init__(world, position, 4, 4)

    def __str__(self):
        return 'Antelope'

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
