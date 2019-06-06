import pygame

from .entities.animal import Animal

from .entities.antelope import Antelope
from .entities.cybersheep import CyberSheep
from .entities.fox import Fox
from .entities.human import Human
from .entities.sheep import Sheep
from .entities.turtle import Turtle
from .entities.wolf import Wolf

from .entities.belladonna import Belladonna
from .entities.dandelion import Dandelion
from .entities.grass import Grass
from .entities.guarana import Guarana
from .entities.hogweed import Hogweed

from .messages import Messages

class World():
    font = pygame.font.Font(None, 24)

    def __init__(self, width, height, pos):
        self.__position = pos
        self.__size = self.__width, self.__height = width, height
        self.__entities = []
        self.__messages = Messages((self.getRect().width + 16, 110))
        self.__human = None
        newEntities = [
            Grass(self, [0, 0]),
            Guarana(self, [7, 17]),
            Belladonna(self, [2, 10]),
            Dandelion(self, [4, 15]),
            Hogweed(self, [0, 1]),
            Hogweed(self, [24, 18]),

            Antelope(self, [20, 3]),
            CyberSheep(self, [24, 1]),
            Fox(self, [3, 5]),
            Sheep(self, [2, 15]),
            Turtle(self, [16, 17]),
            Wolf(self, [5, 12]),

            Human(self, [10, 10])
        ]

        for e in newEntities:
            self.spawnEntity(e, e.position)

    def setHumanDirection(self, dir):
        self.__human.setDirection(dir)

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getRect(self):
        return pygame.Rect(0, 0, 40 + 30 * self.__width, 40 + 30 * self.__height)

    def addMessage(self, message):
        self.__messages.add(message)

    def spawnEntity(self, entity, position):
        e = None
        if isinstance(entity, Belladonna):
            e = Belladonna(self, position)
        elif isinstance(entity, Dandelion):
            e = Dandelion(self, position)
        elif isinstance(entity, Grass):
            e = Grass(self, position)
        elif isinstance(entity, Guarana):
            e = Guarana(self, position)
        elif isinstance(entity, Hogweed):
            e = Hogweed(self, position)
        elif isinstance(entity, Antelope):
            e = Antelope(self, position)
        elif isinstance(entity, CyberSheep):
            e = CyberSheep(self, position)
        elif isinstance(entity, Fox):
            e = Fox(self, position)
        elif isinstance(entity, Human):
            e = Human(self, position)
            self.__human = e
        elif isinstance(entity, Sheep):
            e = Sheep(self, position)
        elif isinstance(entity, Turtle):
            e = Turtle(self, position)
        elif isinstance(entity, Wolf):
            e = Wolf(self, position)

        self.__entities.append(e)
        self.addMessage(str(entity) + ' was spawned at ' + str(position))

    def getClosestHogweed(self, pos):
        closest = (-1, -1)
        distanceX = -1
        distanceY = -1
        for e in self.__entities:
            if e.isAlive and isinstance(e, Hogweed):
                d1x = abs(e.position[0] - pos[0])
                d2x = abs(e.position[0] + (self.__width - pos[0]))
                d1y = abs(e.position[1] - pos[1])
                d2y = abs(e.position[1] + (self.__height - pos[1]))
                dx = d1x if d1x < d2x else d2x
                dy = d1y if d1y < d2y else d2y
                if closest == (-1, -1) or distanceX + distanceY > dx + dy:
                    closest = e.position
                    distanceX = dx
                    distanceY = dy

        return closest

    def getFreeSpaceAround(self, pos):
        positions = [
            (pos[0], pos[1] - 1 if pos[1] > 0 else self.__height - 1),
            (pos[0], (pos[1] + 1) % self.__height),
            (pos[0] - 1 if pos[0] > 0 else self.__width - 1, pos[1]),
            ((pos[0] + 1) % self.__width, pos[1])
        ]
        free = []
        for p in positions:
            isFree = True
            for e in self.__entities:
                if e.isAlive and e.position == p:
                    isFree = False
            if isFree:
                free.append(p)

        return free

    def getEntityAt(self, you, pos):
        for e in self.__entities:
            if e.isAlive and e != you and e.position == pos:
                return e
        return None

    def killAnimalsAround(self, pos):
        positions = [
            (pos[0], pos[1] - 1 if pos[1] > 0 else self.__height - 1),
            (pos[0], (pos[1] + 1) % self.__height),
            (pos[0] - 1 if pos[0] > 0 else self.__width - 1, pos[1]),
            ((pos[0] + 1) % self.__width, pos[1])
        ]
        for p in positions:
            for e in self.__entities:
                if isinstance(e, Animal) and not isinstance(e, CyberSheep) and e.position == p:
                    e.kill()
                    self.addMessage(str(e) + ' was slain by Hogweed')

    def doTurn(self):
        self.__messages.clear()
        self.__entities.sort(reverse=True)
        size = len(self.__entities)
        for i in range(size):
            if self.__entities[i].isAlive:
                self.__entities[i].action()

                e = self.getEntityAt(self.__entities[i], self.__entities[i].position)
                if e:
                    self.__entities[i].collision(e)

                self.__entities[i].increaseLifeTime()

        self.__removeKilledEntities()

    def draw(self, screen):
        color = (200, 200, 200)
        screen.fill(color, pygame.Rect(self.__position, (20, self.getRect().height)))
        screen.fill(color, pygame.Rect(self.getRect().right - 20, self.__position[1], 20, self.getRect().height))
        screen.fill(color, pygame.Rect(self.__position, (self.getRect().width, 20)))
        screen.fill(color, pygame.Rect(self.__position[0], self.getRect().bottom - 20, self.getRect().width, 20))

        offset = (self.__position[0] + 20, self.__position[1] + 20)
        for e in self.__entities:
            if e.isAlive:
                e.draw(screen, offset)

        text = World.font.render('Human direction: ' + self.__human.getDirection(), 1, (240, 240, 240))
        screen.blit(text, (self.getRect().width + 16, 60))

        self.__messages.draw(screen)

    def __removeKilledEntities(self):
        killed = []
        for i in range(len(self.__entities)):
            if not self.__entities[i].isAlive:
                killed.append(i)

        killed.reverse()
        for k in killed:
            self.__entities.pop(k)
