import pygame

pygame.init()

window = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Slash and Survive")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()