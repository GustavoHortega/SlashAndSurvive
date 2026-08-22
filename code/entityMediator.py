class EntityMediator:

    @staticmethod
    def check_collision(player, enemies):
        for enemy in enemies:
            player_collision = player.rect.colliderect(enemy.rect)

            if player_collision:
                player.take_damage(enemy.damage)
                return True

        return False
