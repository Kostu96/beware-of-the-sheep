from .plant import Plant
from .animal import Animal

class Belladonna(Plant):
    color = (200, 0, 50)
    symbol = 'BD'

    def __init__(self, world, position):
        super().__init__(world, position, 99)

    def __str__(self):
        return 'Belladona'

    def collision(self, other):
        if isinstance(other, Animal) and other.strength < self.strength:
            other.kill()
            self.world.addMessage(str(other) + ' was slain by ' + str(self))

    def getColor(self):
        return Belladonna.color

    def getSymbol(self):
        return Belladonna.symbol
