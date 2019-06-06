from .Entities.entities import Entity
from .Entities import animals
from .Entities import plants
import pygame


class World():
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height

        self.entities = [
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
        for e in self.entities:
            if e.isAlive:
                e.action()
