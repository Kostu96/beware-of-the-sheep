import sys
import pygame
from .Entities.entities import Entity
from .Entities import animals
from .Entities import plants


class World():
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height

        self.entities = [
            plants.Grass(self, [0, 0]),
            plants.Guarana(self, [7, 17]),
            plants.Belladonna(self, [2, 10]),
            plants.Dandelion(self, [4, 15]),
            plants.Hogweed(self, [24, 18]),

            animals.Antelope(self, [20, 3]),
            animals.CyberSheep(self, [14, 17]),
            animals.Fox(self, [3, 5]),
            animals.Sheep(self, [2, 15]),
            animals.Turtle(self, [16, 17]),
            animals.Wolf(self, [5, 12]),

            animals.Human(self, [10, 10]),
        ]

    def getRect(self):
        return pygame.Rect(0, 0, 40 + 30 * self.width, 40 + 30 * self.height)

    def _drawEdges(self, screen, offset):
        color = (200, 200, 200)
        screen.fill(color,
                    pygame.Rect(0, 0,
                                20, self.getRect().height))
        screen.fill(color,
                    pygame.Rect(self.getRect().right - 20, 0,
                                20, self.getRect().height))
        screen.fill(color,
                    pygame.Rect(0, 0,
                                self.getRect().width, 20))
        screen.fill(color,
                    pygame.Rect(0, self.getRect().bottom - 20,
                                self.getRect().width, 20))

    def draw(self, screen, offset):
        self._drawEdges(screen, offset)
        offset = (offset[0] + 20, offset[1] + 20)
        for e in self.entities:
            e.draw(screen, offset)

    def _removeKilledEntities(self):
        killed = []
        for i in range(len(self.entities)):
            if not self.entities[i].isAlive:
                killed.append(i)

        for k in killed:
            self.entities.pop(k)

    def doTurn(self):
        self._removeKilledEntities()
        self.entities.sort(reverse=True)
        for e in self.entities:
            if e.isAlive:
                e.action()


class Game():
    pygame.font.init()
    font = pygame.font.Font(None, 24)

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.size = self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(
            'Beware Of The Sheep | Konstanty Misiak 175524'
        )

        self.world = World(25, 19)

        self.turnButtonRect = pygame.Rect(1280 - 120, 20, 100, 30)
        self.turnButtonUnactiveColor = (150, 200, 150)
        self.turnButtonActiveColor = (180, 100, 180)
        self.turnButtonColor = self.turnButtonUnactiveColor
        self.turnButtonText = 'Next Turn'

    def _clear(self):
        color = 30, 30, 60
        self.screen.fill(color)

    def _display(self):
        pygame.display.flip()

    def _render(self):
        self._clear()
        self.world.draw(self.screen, (0, 0))

        text = Game.font.render(self.turnButtonText, 1, (0, 0, 0))
        textpos = text.get_rect(center=self.turnButtonRect.center)
        self.screen.fill(self.turnButtonColor, self.turnButtonRect)
        self.screen.blit(text, textpos)

        self._display()

    def _processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.turnButtonRect.collidepoint(event.pos):
                        self.turnButtonColor = self.turnButtonActiveColor
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.turnButtonColor = self.turnButtonUnactiveColor
                    self.world.doTurn()

    def run(self):
        while 1:
            self._processEvents()
            self._render()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
