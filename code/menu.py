import sys

import pygame
from pygame import Font, Surface, Rect

from code.const import WIN_HEIGHT, WIN_WIDTH, C_WHITE


class Menu:
    def __init__(self, window, caption):
        self.window = window
        pygame.display.set_caption(caption)
        background = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        self.surf = pygame.transform.scale(background, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect()
        title = pygame.image.load('./assets/MenuTitle.png').convert_alpha()
        self.title_surf = pygame.transform.scale_by(title, 0.2)
        self.title_rect = self.title_surf.get_rect(
            centerx=WIN_WIDTH // 2,
            top=80
        )
        self.font = pygame.font.SysFont(
            name="Lucida Sans Typewriter",
            size=35
        )

    def run(self):
        menu_option = 0
        # pygame.mixer.music.load("assets/Menu.mp3")
        # pygame.mixer.play(-1)

        while True:
            # DESENHA
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha a imagem do bg no rect do menu.
            self.window.blit(source=self.title_surf, dest=self.title_rect)

            # TEXTO
            if (pygame.time.get_ticks() // 300) % 2 == 0:
                self.menu_text(
                    'Press space bar to start',
                    C_WHITE,
                    (WIN_WIDTH // 2, WIN_HEIGHT - 100)
                )

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Tutorial.run()

    def menu_text(self, text: str, text_color: tuple, text_center_pos: tuple):
        text_surf = self.font.render(
            text,
            True,
            text_color
        ).convert_alpha()

        text_rect = text_surf.get_rect(
            center=text_center_pos
        )

        self.window.blit(text_surf, text_rect)
