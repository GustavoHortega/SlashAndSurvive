from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name: str, position: tuple, health: int, damage: int):
        self.name = name
        self.direction = 'down'
        self.health = health
        self.damage = damage
        self.position = position
        self.frame = 0
        self.last_update = 0

    @abstractmethod
    def move(self):
        pass

    def animate(self):
        pass
    @abstractmethod
    def attack(self):
        pass