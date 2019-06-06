from .Entities.entities import Entity
from .Entities import animals
from .Entities import plants
import pygame


class World():
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.entities = []
        self.messages = []

        newEntities = [
            plants.Grass(self, [0, 0]),
            plants.Guarana(self, [7, 17]),
            plants.Belladonna(self, [2, 10]),
            plants.Dandelion(self, [4, 15]),
            plants.Hogweed(self, [24, 18]),

            animals.Antelope(self, [20, 3]),
            animals.CyberSheep(self, [14, 17]),
            animals.Fox(self, [3, 5]),
            animals.Sheep(self, [2, 15]),
            animals.Turtle(self, [16, 17]),
            animals.Wolf(self, [5, 12]),

            animals.Human(self, [10, 10]),
        ]

        for e in newEntities:
            self.entities.append(e)

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
            e.draw(screen, offset)

    def _removeKilledEntities(self):
        killed = []
        for i in range(len(self.entities)):
            if not self.entities[i].isAlive:
                killed.append(i)

        for k in killed:
            self.entities.pop(k)

    def doTurn(self):
        self._removeKilledEntities()
        self.entities.sort(reverse=True)
        size = len(self.entities)
        for i in range(size):
            if self.entities[i].isAlive:
                self.entities[i].action()

    def getFreeSpaceAround(self, position):
        positions = [
            (position[0], position[1] - 1 if position[1] > 0 else self.height - 1),
            (position[0], (position[1] + 1) % self.height),
            (position[0] - 1 if position[0] > 0 else self.width - 1, position[1]),
            ((position[0] + 1) % self.width, position[1])
        ]
        free = []
        for p in positions:
            isFree = True
            for e in self.entities:
                if e.position == p:
                    isFree = False
            if isFree:
                free.append(p)

        return free

    def spawnEntity(self, entity, position):
        if isinstance(entity, plants.Belladonna):
            self.entities.append(plants.Belladonna(self, position))
        elif isinstance(entity, plants.Dandelion):
            self.entities.append(plants.Dandelion(self, position))
        elif isinstance(entity, plants.Grass):
            self.entities.append(plants.Grass(self, position))
        elif isinstance(entity, plants.Guarana):
            self.entities.append(plants.Guarana(self, position))
        elif isinstance(entity, plants.Hogweed):
            self.entities.append(plants.Hogweed(self, position))
        elif isinstance(entity, animals.Antelope):
            self.entities.append(animals.Antelope(self, position))
        elif isinstance(entity, animals.CyberSheep):
            self.entities.append(animals.CyberSheep(self, position))
        elif isinstance(entity, animals.Fox):
            self.entities.append(animals.Fox(self, position))
        elif isinstance(entity, animals.Human):
            self.entities.append(animals.Human(self, position))
        elif isinstance(entity, animals.Sheep):
            self.entities.append(animals.Sheep(self, position))
        elif isinstance(entity, animals.Turtle):
            self.entities.append(animals.Turtle(self, position))
        elif isinstance(entity, animals.Wolf):
            self.entities.append(animals.Wolf(self, position))

        self.addMessage(str(entity) + ' was spawned at ' + str(position))

    def addMessage(self, message):
        self.messages.append(message)

    def drawMessages(self, screen, offset):
        pass
