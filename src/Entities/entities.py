from abc import ABC
from abc import abstractmethod


class Entity(ABC):
    def __init__(self):
        super.__init__()

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
