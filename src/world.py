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

class World():
    pygame.font.init()
    font = pygame.font.Font(None, 24)

    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.entities = []
        self.messages = []

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

    def getRect(self):
        return pygame.Rect(0, 0, 40 + 30 * self.width, 40 + 30 * self.height)

    def _drawEdges(self, screen, offset):
        color = (200, 200, 200)
        screen.fill(color,
                    pygame.Rect(0, 0,
                                20, self.getRect().height))
        screen.fill(color,
                    pygame.Rect(self.getRect().right - 20, 0,
                                20, self.getRect().height))
        screen.fill(color,
                    pygame.Rect(0, 0,
                                self.getRect().width, 20))
        screen.fill(color,
                    pygame.Rect(0, self.getRect().bottom - 20,
                                self.getRect().width, 20))

    def draw(self, screen, offset):
        self._drawEdges(screen, offset)
        offset = (offset[0] + 20, offset[1] + 20)
        for e in self.entities:
            if e.isAlive:
                e.draw(screen, offset)

    def _removeKilledEntities(self):
        killed = []
        for i in range(len(self.entities)):
            if not self.entities[i].isAlive:
                killed.append(i)

        for k in killed:
            self.entities.pop(k)

    def doTurn(self):
        self.messages.clear()
        self.entities.sort(reverse=True)
        size = len(self.entities)
        for i in range(size):
            if self.entities[i].isAlive:
                self.entities[i].action()

                e = self.getEntityAt(self.entities[i], self.entities[i].position)
                if e:
                    self.entities[i].collision(e)

                self.entities[i].increaseLifeTime()

        self._removeKilledEntities()

    def getFreeSpaceAround(self, pos):
        positions = [
            (pos[0], pos[1] - 1 if pos[1] > 0 else self.height - 1),
            (pos[0], (pos[1] + 1) % self.height),
            (pos[0] - 1 if pos[0] > 0 else self.width - 1, pos[1]),
            ((pos[0] + 1) % self.width, pos[1])
        ]
        free = []
        for p in positions:
            isFree = True
            for e in self.entities:
                if e.isAlive and e.position == p:
                    isFree = False
            if isFree:
                free.append(p)

        return free

    def getEntityAt(self, you, pos):
        for e in self.entities:
            if e.isAlive and e != you and e.position == pos:
                return e
        return None

    def killAnimalsAround(self, pos):
        positions = [
            (pos[0], pos[1] - 1 if pos[1] > 0 else self.height - 1),
            (pos[0], (pos[1] + 1) % self.height),
            (pos[0] - 1 if pos[0] > 0 else self.width - 1, pos[1]),
            ((pos[0] + 1) % self.width, pos[1])
        ]
        for p in positions:
            for e in self.entities:
                if isinstance(e, Animal) and not isinstance(e, CyberSheep) and e.position == p:
                    e.kill()
                    self.addMessage(str(e) + ' was slain by Hogweed')

    def getClosestHogweed(self, pos):
        closest = (-1, -1)
        distanceX = -1
        distanceY = -1
        for e in self.entities:
            if e.isAlive and isinstance(e, Hogweed):
                d1x = abs(e.position[0] - pos[0])
                d2x = abs(e.position[0] + (self.width - pos[0]))
                d1y = abs(e.position[1] - pos[1])
                d2y = abs(e.position[1] + (self.height - pos[1]))
                dx = d1x if d1x < d2x else d2x
                dy = d1y if d1y < d2y else d2y
                if closest == (-1, -1) or distanceX + distanceY > dx + dy:
                    closest = e.position
                    distanceX = dx
                    distanceY = dy

        return closest

    def spawnEntity(self, entity, position):
        if isinstance(entity, Belladonna):
            self.entities.append(Belladonna(self, position))
        elif isinstance(entity, Dandelion):
            self.entities.append(Dandelion(self, position))
        elif isinstance(entity, Grass):
            self.entities.append(Grass(self, position))
        elif isinstance(entity, Guarana):
            self.entities.append(Guarana(self, position))
        elif isinstance(entity, Hogweed):
            self.entities.append(Hogweed(self, position))
        elif isinstance(entity, Antelope):
            self.entities.append(Antelope(self, position))
        elif isinstance(entity, CyberSheep):
            self.entities.append(CyberSheep(self, position))
        elif isinstance(entity, Fox):
            self.entities.append(Fox(self, position))
        elif isinstance(entity, Human):
            self.entities.append(Human(self, position))
        elif isinstance(entity, Sheep):
            self.entities.append(Sheep(self, position))
        elif isinstance(entity, Turtle):
            self.entities.append(Turtle(self, position))
        elif isinstance(entity, Wolf):
            self.entities.append(Wolf(self, position))

        self.addMessage(str(entity) + ' was spawned at ' + str(position))

    def addMessage(self, message):
        self.messages.append(message)

    def drawMessages(self, screen, offset):
        for m in self.messages:
            text = World.font.render(m, 1, (240, 240, 240))
            screen.blit(text, offset)
            offset = (offset[0], offset[1] + 20)
