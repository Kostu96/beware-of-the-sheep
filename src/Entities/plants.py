from .entities import Plant


class Belladonna(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)

    def getColor(self):
        return (200, 0, 50)

    def getText(self):
        return 'BD'


class Dandelion(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)

    def getColor(self):
        return (255, 255, 0)

    def getText(self):
        return 'DN'


class Grass(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)

    def getColor(self):
        return (0, 255, 0)

    def getText(self):
        return 'GS'


class Guarana(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)

    def getColor(self):
        return (20, 200, 150)

    def getText(self):
        return 'GA'


class Hogweed(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)

    def getColor(self):
        return (255, 165, 0)

    def getText(self):
        return 'HG'
