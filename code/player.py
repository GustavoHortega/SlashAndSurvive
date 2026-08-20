import pygame

from code.const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED
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
        entity_speed = ENTITY_SPEED
        pressedkey = pygame.key.get_pressed()
        if (pressedkey[pygame.K_LEFT] or pressedkey[pygame.K_a]) and self.rect.left > 0:
            self.rect.centerx -= entity_speed
            self.direction = "left"

        if (pressedkey[pygame.K_RIGHT] or pressedkey[pygame.K_d]) and self.rect.right < WIN_WIDTH:
            self.rect.centerx += entity_speed
            self.direction = "right"

        if (pressedkey[pygame.K_UP] or pressedkey[pygame.K_w]) and self.rect.top > 0:
            self.rect.centery -= entity_speed
            self.direction = "up"

        if (pressedkey[pygame.K_DOWN] or pressedkey[pygame.K_s]) and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += entity_speed
            self.direction = "down"

        self.position = self.rect.center

    def attack(self):
        pass
