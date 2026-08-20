from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name: str, position: tuple, health: int, damage: int):
        self.name = name
        self.direction = 'down'
        self.health = health
        self.damage = damage
        self.position = position

    @abstractmethod
    def move(self):
        pass

    def animate(self):
        pass
    @abstractmethod
    def attack(self):
        pass