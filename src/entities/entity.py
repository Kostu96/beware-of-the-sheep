import pygame
import random
from abc import ABC, abstractmethod
from functools import total_ordering

@total_ordering
class Entity(ABC):
    pygame.font.init()
    font = pygame.font.Font(None, 24)

    def __init__(self, world, position, strength, initiative):
        super().__init__()
        self.size = self.width, self.height = 30, 30
        self.world = world
        self.position = self._convertPos(position)
        self.prevPosition = position
        self.isAlive = True
        self.lifeTime = 0
        self.strength = strength
        self.initiative = initiative

    def __eq__(self, other):
        return (self.initiative, self.lifeTime) == (other.initiative, other.lifeTime)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.initiative != other.initiative:
            return self.initiative < other.initiative
        return self.lifeTime < other.lifeTime

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def getColor(self):
        pass

    @abstractmethod
    def getSymbol(self):
        pass

    def draw(self, screen, offset):
        rect = pygame.Rect(offset[0] + self.position[0] * 30,
                           offset[1] + self.position[1] * 30,
                           30, 30)
        text = Entity.font.render(self.getSymbol(), 1, (0, 0, 0))
        textpos = text.get_rect(center=rect.center)

        screen.fill(self.getColor(), rect)
        screen.blit(text, textpos)

    def _convertPos(self, pos):
        if pos[0] < 0:
            posX = self.world.getWidth() + pos[0]
        else:
            posX = pos[0] % self.world.getWidth()

        if pos[1] < 0:
            posY = self.world.getHeight() + pos[1]
        else:
            posY = pos[1] % self.world.getHeight()

        return (posX, posY)

    def move(self, dx, dy):
        self.prevPosition = self.position

        newX = self.position[0] + dx
        newY = self.position[1] + dy

        self.position = self._convertPos((newX, newY))

    def moveToPrevPosition(self):
        self.move(self.prevPosition[0], self.prevPosition[1])

    def dodgedAttack(self, strength):
        return False

    def addStrength(self, amount):
        self.strength += amount

    def increaseLifeTime(self):
        self.lifeTime += 1

    def kill(self):
        self.isAlive = False
