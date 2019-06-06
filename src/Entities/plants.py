from .entities import Plant
import pygame


class Belladonna(Plant):
    color = (200, 0, 50)
    symbol = 'BD'

    def __init__(self, world, position):
        super().__init__(world, position, 99)

    def getColor(self):
        return Belladonna.color

    def getSymbol(self):
        return Belladonna.symbol


class Dandelion(Plant):
    color = (255, 255, 0)
    symbol = 'DN'

    def __init__(self, world, position):
        super().__init__(world, position, 0)

    def getColor(self):
        return Dandelion.color

    def getSymbol(self):
        return Dandelion.symbol


class Grass(Plant):
    color = (00, 220, 20)
    symbol = 'GS'

    def __init__(self, world, position):
        super().__init__(world, position, 0)

    def getColor(self):
        return Grass.color

    def getSymbol(self):
        return Grass.symbol


class Guarana(Plant):
    color = (20, 200, 150)
    symbol = 'GA'

    def __init__(self, world, position):
        super().__init__(world, position, 0)

    def getColor(self):
        return Guarana.color

    def getSymbol(self):
        return Guarana.symbol


class Hogweed(Plant):
    color = (255, 165, 0)
    symbol = 'HG'

    def __init__(self, world, position):
        super().__init__(world, position, 10)

    def getColor(self):
        return Hogweed.color

    def getSymbol(self):
        return Hogweed.symbol
