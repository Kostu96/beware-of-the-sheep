import sys
import pygame
from .Entities.entities import Entity
from .Entities import animals
from .Entities import plants


class World():
    def __init__(self):
        self.entities = [
            
        ]

    def draw(self):
        pass


class Game():
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(
            'Beware Of The Sheep | Konstanty Misiak 175524'
        )

        self.world = World()

    def clear(self):
        color = 30, 30, 60
        self.screen.fill(color)

    def display(self):
        pygame.display.flip()

    def render(self):
        self.clear()
        self.world.draw()
        self.display()

    def processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def run(self):
        while 1:
            self.processEvents()
            self.render()


if __name__ == '__main__':
    game = Game()
    game.run()
