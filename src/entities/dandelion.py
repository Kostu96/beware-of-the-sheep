from .plant import Plant

class Dandelion(Plant):
    color = (255, 255, 0)
    symbol = 'DN'

    def __init__(self, world, position):
        super().__init__(world, position, 0)

    def __str__(self):
        return 'Dandelion'

    def action(self):
        super().action()
        super().action()
        super().action()

    def getColor(self):
        return Dandelion.color

    def getSymbol(self):
        return Dandelion.symbol
