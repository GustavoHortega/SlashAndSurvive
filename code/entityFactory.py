import random

from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player
from code.enemy import Enemy


class EntityFactory:

    @staticmethod
    def get_entity(entity_name):
        if entity_name == "Player":
            return Player(entity_name)
        if entity_name == "Enemy":
            return Enemy(entity_name, (random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT)))
