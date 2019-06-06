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
            Button(pygame.Rect(self.__world.getRect().width + 20, 20, 100, 30),
                   'Next Turn',
                   lambda: self.__world.doTurn()),
            Button(pygame.Rect(self.__world.getRect().width + 140, 20, 100, 30),
                   'Save',
                   None),
            Button(pygame.Rect(self.__world.getRect().width + 260, 20, 100, 30),
                   'Load',
                   None),
        ]

    def run(self):
        while 1:
            self.__processEvents()
            self.__render()
            self.__clock.tick(60)

    def __render(self):
        self.__screen.fill((30, 30, 50))

        self.__world.draw(self.__screen)
        self.__legend.draw(self.__screen)
        for b in self.__buttons:
            b.draw(self.__screen)
        
        pygame.display.flip()

    def __processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for b in self.__buttons:
                        b.handleDownClick(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for b in self.__buttons:
                        b.handleUpClick()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.__world.doTurn()
