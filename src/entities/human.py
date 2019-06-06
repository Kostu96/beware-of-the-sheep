from .animal import Animal

class Human(Animal):
    color = (250, 200, 250)
    symbol = 'HM'

    def __init__(self, world, position):
        super().__init__(world, position, 5, 4)
        self.__direction = None
        self.__isSuperPowerActive = False
        self.__isSuperPowerCoolDown = False
        self.__superPowerLength = 4
        self.__superPowerCooldown = 4

    def __str__(self):
        return 'Human'

    def setDirection(self, dir):
        self.__direction = dir

    def getDirection(self):
        if not self.isAlive:
            return 'dead'
        if self.__direction == None:
            return 'none'
        return self.__direction

    def activateSuperPower(self):
        if self.__isSuperPowerActive or self.__isSuperPowerCoolDown:
            return
        else:
            self.__isSuperPowerActive = True

    def getSuperPowerStatus(self):
        if not self.isAlive:
            return 'dead'
        if self.__isSuperPowerActive:
            return 'active for ' + str(self.__superPowerLength) + ' turns'
        if self.__isSuperPowerCoolDown:
            return 'cooldown for ' + str(self.__superPowerCooldown) + ' turns'
        return 'unactive'

    def action(self):
        if self.__direction == 'up':
            self.move(0, -1)
        elif self.__direction == 'down':
            self.move(0, 1)
        elif self.__direction == 'left':
            self.move(-1, 0)
        elif self.__direction == 'right':
            self.move(1, 0)

        if self.__isSuperPowerActive:
            self.world.killAround(self.position, True)
            if self.__superPowerLength > 1:
                self.__superPowerLength -= 1
            else:
                self.__superPowerLength = 4
                self.__isSuperPowerActive = False
                self.__isSuperPowerCoolDown = True
        elif self.__isSuperPowerCoolDown:
            if self.__superPowerCooldown > 1:
                self.__superPowerCooldown -= 1
            else:
                self.__superPowerCooldown = 4
                self._Human__isSuperPowerCoolDown = False

    def getColor(self):
        return Human.color

    def getSymbol(self):
        return Human.symbol
