import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT, WIN_CAPTION
from code.menu import Menu


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window, WIN_CAPTION)
            menu_return = menu.run()
