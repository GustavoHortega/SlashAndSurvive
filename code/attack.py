import pygame

from code.const import ATTACK_ANIMATION_DELAY


class Attack:
    def __init__(self, player):
        self.direction = player.direction
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.finished = False
        self.animation = {
            'up': [
                pygame.image.load('assets/SlashUp1.png').convert_alpha(),
                pygame.image.load('assets/SlashUp2.png').convert_alpha(),
                pygame.image.load('assets/SlashUp3.png').convert_alpha()
            ],

            'down': [
                pygame.image.load('assets/SlashDown1.png').convert_alpha(),
                pygame.image.load('assets/SlashDown2.png').convert_alpha(),
                pygame.image.load('assets/SlashDown3.png').convert_alpha()
            ],

            'left': [
                pygame.image.load('assets/SlashLeft1.png').convert_alpha(),
                pygame.image.load('assets/SlashLeft2.png').convert_alpha(),
                pygame.image.load('assets/SlashLeft3.png').convert_alpha()
            ],

            'right': [
                pygame.image.load('assets/SlashRight1.png').convert_alpha(),
                pygame.image.load('assets/SlashRight2.png').convert_alpha(),
                pygame.image.load('assets/SlashRight3.png').convert_alpha()
            ]
        }

        self.surf = self.animation[self.direction][self.frame]
        self.rect = self.surf.get_rect()

        if self.direction == "up":
            self.rect.midbottom = player.rect.midtop

        elif self.direction == "down":
            self.rect.midtop = player.rect.midbottom

        elif self.direction == "left":
            self.rect.midright = player.rect.midleft

        elif self.direction == "right":
            self.rect.midleft = player.rect.midright

    def animate(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_update >= ATTACK_ANIMATION_DELAY:
            self.frame += 1
            self.last_update = current_time

            if self.frame >= len(self.animation[self.direction]):
                self.finished = True
                return

            self.surf = self.animation[self.direction][self.frame]