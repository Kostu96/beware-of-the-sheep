from .entities import Plant, Animal
from .animals import CyberSheep
import pygame


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


class Guarana(Plant):
    color = (20, 200, 150)
    symbol = 'GA'

    def __init__(self, world, position):
        super().__init__(world, position, 0)

    def __str__(self):
        return 'Guarana'

    def collision(self, other):
        if isinstance(other, Animal):
            other.addStrength(3)
            self.world.addMessage(str(other) + ' ' + str(other.position) + ' now has ' + str(other.strength) + ' strength')

    def getColor(self):
        return Guarana.color

    def getSymbol(self):
        return Guarana.symbol


class Hogweed(Plant):
    color = (255, 165, 0)
    symbol = 'HG'

    def __init__(self, world, position):
        super().__init__(world, position, 10)

    def __str__(self):
        return 'Hogweed'

    def action(self):
        self.world.killAnimalsAround(self.position)
        super().action()

    def collision(self, other):
        if not isinstance(other, CyberSheep):
            other.kill()
            self.world.addMessage(str(other) + ' was slain by ' + str(self))

    def getColor(self):
        return Hogweed.color

    def getSymbol(self):
        return Hogweed.symbol
