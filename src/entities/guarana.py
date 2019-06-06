from .plant import Plant

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
