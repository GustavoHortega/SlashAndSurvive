from code.attack import Attack
from code.entity import Entity


class EntityMediator:

    @staticmethod
    def check_collision(player, enemies,attack):
        for enemy in enemies:
            player_collision = player.rect.colliderect(enemy.rect)

            if player_collision:
                player.take_damage(enemy.damage)
                return True

            if attack is not None:
                attack_collision = enemy.rect.colliderect(attack.rect)

                if attack_collision:
                    enemy.take_damage(player.damage)

        return False
