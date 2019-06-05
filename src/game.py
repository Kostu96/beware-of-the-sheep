import sys
import pygame
from .Entities.entities import Entity
from .Entities import animals
from .Entities import plants


class World():
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height

        self.entities = [
            plants.Grass(self, [1, 1])
        ]

    def draw(self, screen):
        for e in self.entities:
            e.draw(screen)


class Game():
    def __init__(self):
        pygame.init()

        self.size = self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(
            'Beware Of The Sheep | Konstanty Misiak 175524'
        )

        self.world = World(16, 16)

    def _clear(self):
        color = 30, 30, 60
        self.screen.fill(color)

    def _display(self):
        pygame.display.flip()

    def _render(self):
        self._clear()
        self.world.draw(self.screen)
        self._display()

    def _processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

    def run(self):
        while 1:
            self._processEvents()
            self._render()


if __name__ == '__main__':
    game = Game()
    game.run()
