from .entities import Animal


class Antelope(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 4, 4)

    def getColor(self):
        return (150, 75, 0)

    def getText(self):
        return 'AT'


class CyberSheep(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 11, 4)

    def getColor(self):
        return (184, 3, 255)

    def getText(self):
        return 'CS'


class Fox(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 3, 7)

    def getColor(self):
        return (205, 87, 0)

    def getText(self):
        return 'FX'


class Human(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 5, 4)

    def getColor(self):
        return (250, 200, 250)

    def getText(self):
        return 'HM'


class Sheep(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 4, 4)

    def getColor(self):
        return (250, 250, 250)

    def getText(self):
        return 'SH'


class Turtle(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 2, 1)

    def getColor(self):
        return (30, 90, 30)

    def getText(self):
        return 'TT'


class Wolf(Animal):
    def __init__(self, world, position):
        super().__init__(world, position, 9, 5)

    def getColor(self):
        return (100, 110, 110)

    def getText(self):
        return 'WF'
