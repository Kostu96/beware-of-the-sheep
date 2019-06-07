from .animal import Animal

class Human(Animal):
    color = (250, 200, 250)
    symbol = 'HM'

    def __init__(self, world, position):
        super().__init__(world, position, 5, 4)
        self.direction = None
        self.isSuperPowerActive = False
        self.isSuperPowerCoolDown = False
        self.superPowerLength = 4
        self.superPowerCooldown = 4

    def __str__(self):
        return 'Human'

    def __repr__(self):
        string = super().__repr__() + '\n'
        string += self.getDirection() + '\n'
        string += str(self.isSuperPowerActive) + '\n'
        string += str(self.isSuperPowerCoolDown) + '\n'
        string += str(self.superPowerLength) + '\n'
        string += str(self.superPowerCooldown)
        return string

    def setDirection(self, dir):
        self.direction = dir

    def getDirection(self):
        if not self.isAlive:
            return 'dead'
        if self.direction == None:
            return 'none'
        return self.direction

    def activateSuperPower(self):
        if self.isSuperPowerActive or self.isSuperPowerCoolDown:
            return
        else:
            self.isSuperPowerActive = True

    def getSuperPowerStatus(self):
        if not self.isAlive:
            return 'dead'
        if self.isSuperPowerActive:
            return 'active for ' + str(self.superPowerLength) + ' turns'
        if self.isSuperPowerCoolDown:
            return 'cooldown for ' + str(self.superPowerCooldown) + ' turns'
        return 'unactive'

    def action(self):
        if self.direction == 'up':
            self.move(0, -1)
        elif self.direction == 'down':
            self.move(0, 1)
        elif self.direction == 'left':
            self.move(-1, 0)
        elif self.direction == 'right':
            self.move(1, 0)

        if self.isSuperPowerActive:
            self.world.killAround(self.position, True)
            if self.superPowerLength > 1:
                self.superPowerLength -= 1
            else:
                self.superPowerLength = 4
                self.isSuperPowerActive = False
                self.isSuperPowerCoolDown = True
        elif self.isSuperPowerCoolDown:
            if self.superPowerCooldown > 1:
                self.superPowerCooldown -= 1
            else:
                self.superPowerCooldown = 4
                self.isSuperPowerCoolDown = False

    def getColor(self):
        return Human.color

    def getSymbol(self):
        return Human.symbol
