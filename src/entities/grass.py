from .plant import Plant

class Grass(Plant):
    color = (00, 220, 20)
    symbol = 'GS'

    def __init__(self, world, position):
        super().__init__(world, position, 0)

    def __str__(self):
        return 'Grass'

    def getColor(self):
        return Grass.color

    def getSymbol(self):
        return Grass.symbol
