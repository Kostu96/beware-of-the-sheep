from .entities import Plant


class Belladonna(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)


class Dandelion(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)


class Grass(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)

    def getColor(self):
        return (0, 255, 0)


class Guarana(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)


class Hogweed(Plant):
    def __init__(self, world, position):
        super().__init__(world, position)
