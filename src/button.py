import pygame

class Button():
    font = pygame.font.Font(None, 24)
    unactiveColor = (150, 200, 150)
    activeColor = (180, 100, 180)

    def __init__(self, rect, text, action):
        self.rect = rect
        self.text = text
        self.action = action
        self.isActive = False
        self.color = Button.unactiveColor

    def draw(self, screen):
        text = Button.font.render(self.text, 1, (0, 0, 0))
        textpos = text.get_rect(center=self.rect.center)
        screen.fill(self.color, self.rect)
        screen.blit(text, textpos)

    def handleDownClick(self, pos):
        if self.rect.collidepoint(pos):
            self.isActive = True
            self.color = Button.activeColor

    def handleUpClick(self):
        if self.isActive:
            self.action()
            self.isActive = False
            self.color = Button.unactiveColor
