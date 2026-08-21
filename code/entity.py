from abc import ABC, abstractmethod

import pygame
from pygame import key

from code.const import SPRITE_ANIMATION_DELAY


class Entity(ABC):
    def __init__(self, name: str, position: tuple, health: int, damage: int):
        self.name = name
        self.direction = 'down'
        self.health = health
        self.damage = damage
        self.position = position
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.is_moving = False

    @abstractmethod
    def move(self):
        pass

    def animate(self):
        if self.is_moving == True:
            if self.direction == 'up':
                self.surf = self.animations["up"]['walk'][self.frame]
            if self.direction == 'down':
                self.surf = self.animations["down"]['walk'][self.frame]
            if self.direction == 'left':
                self.surf = self.animations["left"]['walk'][self.frame]
            if self.direction == 'right':
                self.surf = self.animations["right"]['walk'][self.frame]
        if self.is_moving == False:
            if self.direction == 'up':
                self.surf = self.animations["up"]['idle']
            if self.direction == 'down':
                self.surf = self.animations["down"]['idle']
            if self.direction == 'left':
                self.surf = self.animations["left"]['idle']
            if self.direction == 'right':
                self.surf = self.animations["right"]['idle']
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= SPRITE_ANIMATION_DELAY:
            if self.frame >= 1:
                self.frame = 0
            else:
                self.frame += 1
            self.last_update = current_time

    @abstractmethod
    def attack(self):
        pass
