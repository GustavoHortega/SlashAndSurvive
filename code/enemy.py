import pygame


from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name, positon):
        super().__init__(
            name,
            position=positon,
            health=100,
            damage=10
        )

        self.surf = pygame.image.load('assets/PlayerUpIdle.png').convert_alpha()
        self.rect = self.surf.get_rect(
            center=self.position,
        )

    def move(self):
        pass

    def attack(self):
        pass
