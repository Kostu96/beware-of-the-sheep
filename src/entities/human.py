from .animal import Animal

class Human(Animal):
    color = (250, 200, 250)
    symbol = 'HM'

    def __init__(self, world, position):
        super().__init__(world, position, 5, 4)
        self.__direction = None

    def __str__(self):
        return 'Human'

    def setDirection(self, dir):
        self.__direction = dir

    def getDirection(self):
        if self.__direction == None:
            return 'None'
        else:
            return self.__direction

    def action(self):
        if self.__direction == 'up':
            self.move(0, -1)
        elif self.__direction == 'down':
            self.move(0, 1)
        elif self.__direction == 'left':
            self.move(-1, 0)
        elif self.__direction == 'right':
            self.move(1, 0)

    def getColor(self):
        return Human.color

    def getSymbol(self):
        return Human.symbol
