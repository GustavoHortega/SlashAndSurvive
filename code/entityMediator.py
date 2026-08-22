import pygame

from code.const import PLAYER_DAMAGE_COOLDOWN


class EntityMediator:

    @staticmethod
    def check_collision(player, enemies, attack):
        current_time = pygame.time.get_ticks()
        for enemy in enemies:
            player_collision = player.rect.colliderect(enemy.rect)

            if player_collision:
                if current_time - player.last_damage >= PLAYER_DAMAGE_COOLDOWN:
                    player.take_damage(enemy.damage)
                    player.last_damage = current_time
                return True

            if attack is not None:
                attack_collision = enemy.rect.colliderect(attack.rect)

                if attack_collision:
                    enemy.take_damage(player.damage)

        return False
