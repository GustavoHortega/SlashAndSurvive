import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window):
        self.window = window
        ground = pygame.image.load('./assets/GroundBg.png').convert_alpha()
        self.surf = pygame.transform.scale(ground, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.player = EntityFactory.get_entity('Player')
        self.enemy = EntityFactory.get_entity('Enemy')

    def run(self):
        while True:
            self.window.blit(self.surf, self.rect)
            self.window.blit(self.player.surf, self.player.rect)
            self.window.blit(self.enemy.surf, self.enemy.rect)

            pygame.display.flip()
