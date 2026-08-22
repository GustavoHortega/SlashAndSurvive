import pygame
from pygame import key

from code.attack import Attack
from code.const import WIN_HEIGHT, WIN_WIDTH, PLAYER_SPEED, ATTACK_COOLDOWN
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

        self.last_attack = 0

    def move(self):
        self.is_moving = False
        entity_speed = PLAYER_SPEED
        pressed_key = pygame.key.get_pressed()
        if (pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]) and self.rect.left > 0:
            self.rect.centerx -= entity_speed
            self.direction = "left"
            self.is_moving = True

        if (pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]) and self.rect.right < WIN_WIDTH:
            self.rect.centerx += entity_speed
            self.direction = "right"
            self.is_moving = True

        if (pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]) and self.rect.top > 0:
            self.rect.centery -= entity_speed
            self.direction = "up"
            self.is_moving = True

        if (pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]) and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += entity_speed
            self.direction = "down"
            self.is_moving = True

        self.position = self.rect.center

    def attack(self):
        pressed_key = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()

        if pressed_key[pygame.K_LCTRL] or pressed_key[pygame.K_RCTRL]:
            if current_time - self.last_attack >= ATTACK_COOLDOWN:
                self.last_attack = current_time
                return Attack(self)

        return None