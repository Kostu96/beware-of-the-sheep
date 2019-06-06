import pygame

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

class Legend():
    font = pygame.font.Font(None, 24)

    def __init__(self, world, pos):
        self.__position = pos
        self.__entities = [
            Belladonna(world, [0, 0]),
            Dandelion(world, [0, 0]),
            Grass(world, [0, 0]),
            Guarana(world, [0, 0]),
            Hogweed(world, [0, 0]),
            Antelope(world, [0, 0]),
            Fox(world, [0, 0]),
            Sheep(world, [0, 0]),
            Turtle(world, [0, 0]),
            Wolf(world, [0, 0]),
            CyberSheep(world, [0, 0]),
            Human(world, [0, 0])
    ]

    def draw(self, screen):
        offset = (self.__position[0], self.__position[1] + 5)
        text = Legend.font.render('Legend:', 1, (240, 240, 240))
        screen.blit(text, offset)
        offset = (offset[0], offset[1] - 10)

        i = 0
        for e in self.__entities:
            offset = (offset[0], offset[1] + 32)
            e.draw(screen, offset)
            text = Legend.font.render(str(e), 1, (240, 240, 240))
            screen.blit(text, (offset[0] + 40, offset[1] + 6))
            i += 1
            if (i % 5 == 0):
                offset = (offset[0] + 150, offset[1] - 5 * 32)
