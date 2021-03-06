from .animal import Animal
import random

class Turtle(Animal):
    color = (30, 90, 30)
    symbol = 'TT'

    def __init__(self, world, position):
        super().__init__(world, position, 2, 1)

    def __str__(self):
        return 'Turtle'

    def action(self):
        if random.randint(0, 3) == 0:
            super().action()

    def dodgedAttack(self, strength):
        return strength < 5

    def getColor(self):
        return Turtle.color

    def getSymbol(self):
        return Turtle.symbol
