import sys

import pygame
from pygame import event

from code.const import WIN_WIDTH, WIN_HEIGHT


class Tutorial:
    def __init__(self, window):
        self.window = window
        background = pygame.image.load('./assets/TutorialBg.png').convert_alpha()
        self.surf = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return 2