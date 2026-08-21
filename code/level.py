import sys

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
        self.enemies = []
        self.last_enemy_spawn = pygame.time.get_ticks()

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()

            self.window.blit(self.surf, self.rect)
            self.window.blit(self.player.surf, self.player.rect)

            self.player.move()
            self.player.animate()

            if current_time - self.last_enemy_spawn >= 1000:
                self.enemies.append(
                    EntityFactory.get_entity('Enemy')
                )
                self.last_enemy_spawn = current_time

            for enemy in self.enemies:
                enemy.move(self.player)
                enemy.animate()
                self.window.blit(enemy.surf, enemy.rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
