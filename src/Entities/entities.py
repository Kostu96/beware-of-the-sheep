from abc import ABC
from abc import abstractmethod
import pygame
import random


class Entity(ABC):
    pygame.font.init()
    font = pygame.font.Font(None, 24)

    def __init__(self, world, position):
        super().__init__()
        self.size = self.width, self.height = 30, 30
        self.world = world
        self.position = self._convertPos(position)
        self.prevPosition = position

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
    def getText(self):
        pass

    def draw(self, screen, offset):
        rect = pygame.Rect(offset[0] + self.position[0] * 30,
                           offset[1] + self.position[1] * 30,
                           30, 30)
        text = Entity.font.render(self.getText(), 1, (0, 0, 0))
        textpos = text.get_rect(center=rect.center)

        screen.fill(self.getColor(), rect)
        screen.blit(text, textpos)

    def _convertPos(self, pos):
        if pos[0] < 0:
            pos[0] = self.world.width + pos[0]
        else:
            pos[0] = pos[0] % self.world.width

        if pos[1] < 0:
            pos[1] = self.world.height + pos[1]
        else:
            pos[1] = pos[1] % self.world.height

        return pos

    def move(self, dx, dy):
        self.prevPosition = self.position

        newX = self.position[0] + dx
        newY = self.position[1] + dy

        self.position = self._convertPos((newX, newY))

    def moveToPrevPosition(self):
        self.move(self.prevPosition[0], self.prevPosition[1])


class Plant(Entity):
    def __init__(self, world, position):
        super().__init__(world, position)

    def action(self):
        pass

    def collision(self, other):
        pass


class Animal(Entity):
    def __init__(self, world, position):
        super().__init__(world, position)

    def action(self):
        v_or_h = random.randint(0, 1)
        n_or_p = random.randint(0, 1)

        if v_or_h == 1:
            self.move(0, -1 if n_or_p == 1 else 1)
        else:
            self.move(-1 if n_or_p == 1 else 1, 0)

    def collision(self, other):
        pass
