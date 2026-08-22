import pygame

from code.const import ENEMY_SPEED
from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name, position):
        super().__init__(
            name,
            position=position,
            health=100,
            damage=10
        )

        self.surf = pygame.image.load('assets/PlayerUpIdle.png').convert_alpha()
        self.rect = self.surf.get_rect(
            center=self.position,
        )

        self.animations = {
            "down": {
                "idle": pygame.image.load("assets/PlayerDownIdle.png").convert_alpha(),
                "walk": [
                    pygame.image.load("assets/PlayerDownWalk1.png").convert_alpha(),
                    pygame.image.load("assets/PlayerDownWalk2.png").convert_alpha()
                ]
            },

            "up": {
                "idle": pygame.image.load("assets/PlayerUpIdle.png").convert_alpha(),
                "walk": [
                    pygame.image.load("assets/PlayerUpWalk1.png").convert_alpha(),
                    pygame.image.load("assets/PlayerUpWalk2.png").convert_alpha()
                ]
            },

            "left": {
                "idle": pygame.image.load("assets/PlayerLeftIdle.png").convert_alpha(),
                "walk": [
                    pygame.image.load("assets/PlayerLeftWalk1.png").convert_alpha(),
                    pygame.image.load("assets/PlayerLeftWalk2.png").convert_alpha()
                ]
            },

            "right": {
                "idle": pygame.image.load("assets/PlayerRightIdle.png").convert_alpha(),
                "walk": [
                    pygame.image.load("assets/PlayerRightWalk1.png").convert_alpha(),
                    pygame.image.load("assets/PlayerRightWalk2.png").convert_alpha()
                ]
            }
        }

    def move(self, player):
        self.is_moving = False
        entity_speed = ENEMY_SPEED

        if self.rect.centerx < player.rect.centerx:
            self.rect.centerx += entity_speed
            self.direction = "right"
            self.is_moving = True

        elif self.rect.centerx > player.rect.centerx:
            self.rect.centerx -= entity_speed
            self.direction = "left"
            self.is_moving = True

        if self.rect.centery < player.rect.centery:
            self.rect.centery += entity_speed
            self.direction = "down"
            self.is_moving = True

        elif self.rect.centery > player.rect.centery:
            self.rect.centery -= entity_speed
            self.direction = "up"
            self.is_moving = True

        self.position = self.rect.center
