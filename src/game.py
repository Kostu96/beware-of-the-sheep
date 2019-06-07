import sys
import pygame
pygame.init()

from .world import World
from .legend import Legend
from .button import Button

class Game():
    def __init__(self):
        self.__clock = pygame.time.Clock()
        self.__size = self.__width, self.__height = 1280, 800
        self.__screen = pygame.display.set_mode(self.__size)
        pygame.display.set_caption(
            'Beware Of The Sheep | Konstanty Misiak 175524'
        )

        self.__world = World(25, 19, (0, 0))
        self.__legend = Legend(self.__world, (0, self.__world.getRect().height))
        self.__buttons = [
            Button(pygame.Rect(self.__world.getRect().width + 20, 10, 100, 30),
                   'Next Turn',
                   lambda: self.__world.doTurn()),
            Button(pygame.Rect(self.__world.getRect().width + 140, 10, 100, 30),
                   'Save',
                   lambda: self.__save()),
            Button(pygame.Rect(self.__world.getRect().width + 260, 10, 100, 30),
                   'Load',
                   lambda: self.__load()),
        ]

    def run(self):
        while 1:
            self.__processEvents()
            self.__render()
            self.__clock.tick(60)

    def __save(self):
        pass

    def __load(self):
        pass

    def __render(self):
        self.__screen.fill((30, 30, 50))

        self.__legend.draw(self.__screen)
        self.__world.draw(self.__screen)
        for b in self.__buttons:
            b.draw(self.__screen)
        
        pygame.display.flip()

    def __processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.__world.handleLeftClick(event.pos)
                    for b in self.__buttons:
                        b.handleDownClick(event.pos)
                elif event.button == 3:
                    self.__world.handleRightClick(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for b in self.__buttons:
                        b.handleUpClick()
            elif event.type == pygame.MOUSEMOTION:
                self.__world.handleMouseMoved(event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.__save()
                elif event.key == pygame.K_l:
                    self.__load()
                elif event.key == pygame.K_SPACE:
                    self.__world.doTurn()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.__world.setHumanDirection('up')
                elif event.key == pygame.K_DOWN:
                    self.__world.setHumanDirection('down')
                elif event.key == pygame.K_LEFT:
                    self.__world.setHumanDirection('left')
                elif event.key == pygame.K_RIGHT:
                    self.__world.setHumanDirection('right')
                elif event.key == pygame.K_BACKSPACE:
                    self.__world.setHumanDirection(None)
                elif event.key == pygame.K_RETURN:
                    self.__world.activateHumanSuperPower()
