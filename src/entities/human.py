from .animal import Animal

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
