import pygame

class Button():
    font = pygame.font.Font(None, 24)
    unactiveColor = (150, 200, 150)
    activeColor = (180, 100, 180)

    def __init__(self, rect, text, action):
        self.__rect = rect
        self.__text = text
        self.__action = action
        self.__isActive = False
        self.__color = Button.unactiveColor

    def draw(self, screen):
        text = Button.font.render(self.__text, 1, (0, 0, 0))
        textpos = text.get_rect(center=self.__rect.center)
        screen.fill(self.__color, self.__rect)
        screen.blit(text, textpos)

    def handleDownClick(self, pos):
        if self.__rect.collidepoint(pos):
            self.__isActive = True
            self.__color = Button.activeColor

    def handleUpClick(self):
        if self.__isActive:
            self.__action()
            self.__isActive = False
            self.__color = Button.unactiveColor
