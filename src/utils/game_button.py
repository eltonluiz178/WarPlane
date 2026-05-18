import pygame


class GameButton:
    def __init__(self, screen, text, rect, seta):

        self.screen = screen

        self.text = text
        self.rect = rect
        self.seta = seta

        self.font = pygame.font.Font(
            "assets/fonts/press_start_regular.ttf",
            12
        )

        self.selected = False

    def draw(self):
        x = self.rect.x
        y = self.rect.y

        mouse_pos = pygame.mouse.get_pos()

        hovered = self.rect.collidepoint(mouse_pos)

        active = hovered or self.selected

        # Cores
        if active:
            bg_color = (168, 78, 18)
            border_color = (255, 170, 70)
            text_color = (255, 245, 220)
            arrow_color = (255, 140, 0)
        else:
            bg_color = (18, 18, 18)
            border_color = (90, 90, 50)
            text_color = (230, 230, 230)

        # Fundo principal
        pygame.draw.rect(
            self.screen,
            bg_color,
            self.rect,
            border_radius=4
        )

        # Borda externa
        pygame.draw.rect(
            self.screen,
            border_color,
            self.rect,
            width=2,
            border_radius=4
        )

        # Linha interna
        inner_rect = self.rect.inflate(-8, -8)

        pygame.draw.rect(
            self.screen,
            (60, 60, 40),
            inner_rect,
            width=1,
            border_radius=2
        )

        # Seta apenas no hover se for chamado com seta verdadeiro
        if self.seta == 1:
            if active:
                points = [
                    (x + 14, y + 29),
                    (x + 24, y + 22),
                    (x + 24, y + 36)
                ]

                pygame.draw.polygon(
                    self.screen,
                    arrow_color,
                    points
                )

        # Texto
        label = self.font.render(
            self.text,
            True,
            text_color
        )

        text_rect = label.get_rect(
            center=self.rect.center
        )

        self.screen.blit(label, text_rect)