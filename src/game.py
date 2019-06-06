import sys
import pygame
from .world import World
from .Entities import animals
from .Entities import plants
from .button import Button


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

        self.buttons = [
            Button(pygame.Rect(self.world.getRect().width + 20, 20, 100, 30),
                   'Next Turn',
                   lambda: self.world.doTurn()),
            Button(pygame.Rect(self.world.getRect().width + 140, 20, 100, 30),
                   'Save',
                   None),
            Button(pygame.Rect(self.world.getRect().width + 260, 20, 100, 30),
                   'Load',
                   None),
        ]

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
            text = Game.font.render(str(e), 1, (240, 240, 240))
            screen.blit(text, (offset[0] + 40, offset[1] + 6))
            i += 1
            if (i % 5 == 0):
                offset = (offset[0] + 150, offset[1] - 5 * 32)

    def _render(self):
        self._clear()
        self.world.draw(self.screen, (0, 0))
        self._drawLegend(self.screen, (0, self.world.getRect().height))

        for b in self.buttons:
            b.draw(self.screen)

        text = Game.font.render('Messages:', 1, (240, 240, 240))
        self.screen.blit(text, (self.world.getRect().width + 16, 70))
        self.world.drawMessages(self.screen, (self.world.getRect().width + 20, 100))

        self._display()

    def _processEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for b in self.buttons:
                        b.handleDownClick(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for b in self.buttons:
                        b.handleUpClick()

    def run(self):
        while 1:
            self._processEvents()
            self._render()
            self.clock.tick(60)


if __name__ == '__main__':
    game = Game()
    game.run()
