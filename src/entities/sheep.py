from .animal import Animal

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
