import sys
import pygame


def clear():
    black = 0, 0, 0
    screen.fill(black)


def display():
    pygame.display.flip()


def processEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def render():
    clear()

    display()


pygame.init()

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

while 1:
    processEvents()
    render()
