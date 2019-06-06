from .plant import Plant
from .cybersheep import CyberSheep

class Hogweed(Plant):
    color = (255, 165, 0)
    symbol = 'HG'

    def __init__(self, world, position):
        super().__init__(world, position, 10)

    def __str__(self):
        return 'Hogweed'

    def action(self):
        self.world.killAround(self.position, False)
        super().action()

    def collision(self, other):
        if not isinstance(other, CyberSheep):
            other.kill()
            self.world.addMessage(str(other) + ' was slain by ' + str(self))

    def getColor(self):
        return Hogweed.color

    def getSymbol(self):
        return Hogweed.symbol
