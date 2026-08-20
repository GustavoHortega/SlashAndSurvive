import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH
from code.entity import Entity


class Player(Entity):

    def __init__(self, name):
        super().__init__(
            name,
            position=(WIN_WIDTH // 2, WIN_HEIGHT // 2),
            health=100,
            damage=10
        )

        self.surf = pygame.image.load('assets/PlayerDownIdle.png').convert_alpha()
        self.rect = self.surf.get_rect(
            center=self.position,
        )

    def move(self):
        pass

    def attack(self):
        pass