from abc import ABC
from abc import abstractmethod
from pygame import Rect


class Entity(ABC):
    def __init__(self, world, position):
        super().__init__()
        self.size = self.width, self.height = 30, 30
        self.world = world

        if position[0] < 0:
            position[0] = world.width - position[0]
        else:
            position[0] = position[0] % world.width

        if position[1] < 0:
            position[1] = world.height - position[1]
        else:
            position[1] = position[1] % world.height

        self.position = position
        self.prevPosition = position

    @abstractmethod
    def action(selft):
        pass

    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def getColor(self):
        pass

    def draw(self, screen):
        screen.fill(self.getColor(),
                    Rect((self.position[0] * 30,
                          self.position[1] * 30),
                    self.size))


class Plant(Entity):
    def __init__(self, world, position):
        super().__init__(world, position)

    def action(self):
        pass

    def collision(self, other):
        pass


class Animal(Entity):
    def __init__(self, world, position):
        super().__init__()

    def action(self):
        pass

    def collision(self, other):
        pass
