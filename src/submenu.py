import pygame

from .entities.antelope import Antelope
from .entities.cybersheep import CyberSheep
from .entities.fox import Fox
from .entities.sheep import Sheep
from .entities.turtle import Turtle
from .entities.wolf import Wolf

from .entities.belladonna import Belladonna
from .entities.dandelion import Dandelion
from .entities.grass import Grass
from .entities.guarana import Guarana
from .entities.hogweed import Hogweed

class SubMenu():
    font = pygame.font.Font(None, 24)

    def __init__(self, world):
        self.type = 'empty'
        self.__emptyButtons = [
            'Belladonna',
            'Dandelion',
            'Grass',
            'Guarana',
            'Hogweed',
            'Antelope',
            'Cyber Sheep',
            'Fox',
            'Sheep',
            'Turtle',
            'Wolf'
        ]
        self.__hoverPos = -1
        self.__drawHover = False
        self.choosedPos = ()
        self.__world = world

    def getRect(self, pos):
        if self.type == 'entity':
            return pygame.Rect(pos, (80, 20))
        elif self.type == 'empty':
            return pygame.Rect(pos, (120, len(self.__emptyButtons) * 20))

    def handleLeftClick(self):
        if self.type == 'empty':
            if self.__emptyButtons[self.__hoverPos] == 'Belladonna':
                self.__world.spawnEntity(Belladonna(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Dandelion':
                self.__world.spawnEntity(Dandelion(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Grass':
                self.__world.spawnEntity(Grass(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Guarana':
                self.__world.spawnEntity(Guarana(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Hogweed':
                self.__world.spawnEntity(Hogweed(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Antelope':
                self.__world.spawnEntity(Antelope(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Cyber Sheep':
                self.__world.spawnEntity(CyberSheep(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Fox':
                self.__world.spawnEntity(Fox(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Sheep':
                self.__world.spawnEntity(Sheep(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Turtle':
                self.__world.spawnEntity(Turtle(self.__world, [0, 0]), self.choosedPos)
            if self.__emptyButtons[self.__hoverPos] == 'Wolf':
                self.__world.spawnEntity(Wolf(self.__world, [0, 0]), self.choosedPos)
        elif self.__drawHover:
            self.__world.removeEntityAt(self.choosedPos)

    def handleMouseMoved(self, pos, mousePos):
        if self.getRect(pos).collidepoint(mousePos):
            self.__drawHover = True
            self.__hoverPos = (mousePos[1] - pos[1]) // 20
        else:
            self.__drawHover = False

    def draw(self, screen, pos):
        background = pygame.Surface(self.getRect(pos).size)
        background.convert()
        background.fill((0, 40, 10))
        if self.__drawHover:
            background.fill((60, 100, 60), pygame.Rect(0, self.__hoverPos * 20, self.getRect(pos).width, 20))
        offset = (10, 0)
        if self.type == 'empty':
            for b in self.__emptyButtons:
                text = SubMenu.font.render(b, 1, (240, 240, 240))
                background.blit(text, offset)
                offset = (offset[0], offset[1] + 20)
        else:
            text = SubMenu.font.render('Delete', 1, (240, 240, 240))
            background.blit(text, offset)
        screen.blit(background, pos)
