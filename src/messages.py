import pygame

class Messages():
    font = pygame.font.Font(None, 24)

    def __init__(self, pos):
        self.__position = pos
        self.__messages = []

    def clear(self):
        self.__messages.clear()

    def add(self, message):
        self.__messages.append(message)

    def draw(self, screen):
        offset = self.__position
        text = Messages.font.render('Messages:', 1, (240, 240, 240))
        screen.blit(text, offset)
        offset = (offset[0], offset[1] + 20)
        for m in self.__messages:
            text = Messages.font.render(m, 1, (240, 240, 240))
            screen.blit(text, offset)
            offset = (offset[0], offset[1] + 20)
