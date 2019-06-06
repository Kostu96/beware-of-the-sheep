import sys
import pygame
from .world import World
from .Entities import animals
from .Entities import plants


class Game():
    pygame.font.init()
    font = pygame.font.Font(None, 24)

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.size = self.width, self.height = 1280, 800
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

    def _drawLegend(self, screen, offset):
        entities = [
            plants.Belladonna(self, [0, 0]),
            plants.Dandelion(self, [0, 0]),
            plants.Grass(self, [0, 0]),
            plants.Guarana(self, [0, 0]),
            plants.Hogweed(self, [0, 0]),
            animals.Antelope(self, [0, 0]),
            animals.Fox(self, [0, 0]),
            animals.Sheep(self, [0, 0]),
            animals.Turtle(self, [0, 0]),
            animals.Wolf(self, [0, 0]),
            animals.CyberSheep(self, [0, 0]),
            animals.Human(self, [0, 0])
        ]

        offset = (offset[0], offset[1] + 5)
        text = Game.font.render('Legend:', 1, (240, 240, 240))
        screen.blit(text, offset)
        offset = (offset[0], offset[1] - 10)

        i = 0
        for e in entities:
            offset = (offset[0], offset[1] + 32)
            e.draw(screen, offset)
            text = Game.font.render(e.__class__.__name__, 1, (240, 240, 240))
            screen.blit(text, (offset[0] + 40, offset[1] + 6))
            i += 1
            if (i % 5 == 0):
                offset = (offset[0] + 150, offset[1] - 5 * 32)

    def _render(self):
        self._clear()
        self.world.draw(self.screen, (0, 0))
        self._drawLegend(self.screen, (0, self.world.getRect().height))

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
