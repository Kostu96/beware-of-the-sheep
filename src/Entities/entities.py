from abc import ABC
from abc import abstractmethod


class Entity(ABC):
    def __init__(self, world, position):
        super.__init__()
        self.size = self.width, self.height = 30, 30

        if position.first < 0:
            position.first = world.width - position.first
        else:
            position.first = position.first % world.width

        if position.second < 0:
            position.second = world.height - position.second
        else:
            position.second = position.second % world.height

        self.position = position
        self.prevPosition = position

    @abstractmethod
    def action(selft):
        pass

    @abstractmethod
    def collision(self, other):
        pass


class Plant(Entity):
    def __init__(self):
        super.__init__()

    def action(self):
        pass

    def collision(self, other):
        pass


class Animal(Entity):
    def __init__(self):
        super.__init__()

    def action(self):
        pass

    def collision(self, other):
        pass
