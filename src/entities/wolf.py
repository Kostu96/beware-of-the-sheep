from .animal import Animal

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
