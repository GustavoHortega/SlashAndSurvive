import sys

import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH, C_WHITE
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator


class Level:
    def __init__(self, window):
        self.window = window
        ground = pygame.image.load('./assets/GroundBg.png').convert_alpha()
        self.surf = pygame.transform.scale(ground, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()
        self.player = EntityFactory.get_entity('Player')
        self.enemies = []
        self.last_enemy_spawn = pygame.time.get_ticks()
        self.attack = None

        self.font = pygame.font.SysFont(
            name="Lucida Sans Typewriter",
            size=35
        )

    def run(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            current_time = pygame.time.get_ticks()

            # PLAYER
            self.player.move()
            self.player.animate()

            # ATTACK
            if self.attack is None:
                self.attack = self.player.attack()

            if self.attack is not None:
                self.attack.animate()

                if self.attack.finished:
                    self.attack = None

            # SPAWN
            if current_time - self.last_enemy_spawn >= 1000:
                self.enemies.append(
                    EntityFactory.get_entity('Enemy')
                )
                self.last_enemy_spawn = current_time

            # ENEMIES
            for enemy in self.enemies:
                enemy.move(self.player)
                enemy.animate()

            # COLLISION
            EntityMediator.check_collision(
                self.player,
                self.enemies
            )

            # DESENHA O FUNDO
            self.window.blit(self.surf, self.rect)

            # DESENHA PLAYER
            self.window.blit(
                self.player.surf,
                self.player.rect
            )

            # DESENHA ENEMIES
            for enemy in self.enemies:
                self.window.blit(
                    enemy.surf,
                    enemy.rect
                )

            # DESENHA ATTACK
            if self.attack is not None:
                self.window.blit(
                    self.attack.surf,
                    self.attack.rect
                )

            # HUD
            self.hud(
                text=f"HP: {self.player.health}",
                text_color=C_WHITE,
                text_center_pos=(70, 30)
            )

            pygame.display.flip()

            if self.player.health <= 0:
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def hud(self, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = self.font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect = text_surf.get_rect(
            center=text_center_pos
        )

        self.window.blit(text_surf, text_rect)
