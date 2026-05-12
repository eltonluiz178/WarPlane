import pygame

from core.window import Window
from core.settings import Settings

class PauseScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.window = Window(self.settings)

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        center = (screen_width // 2, screen_height // 2)
        button_width = 260
        button_height = 60

        self.play_button = pygame.Rect(center[0] - button_width / 2, center[1] - button_height, 260, 58)

        self.menu_button = pygame.Rect(center[0] - button_width / 2, center[1] + button_height, 260, 58)

        self.font = pygame.font.Font(
            "assets/fonts/press_start_regular.ttf",
            12
        )

    def update(self):
        pass

    def draw(self):
        """Desenha tudo na tela"""
        self.window.update()  # pygame.display.update()

        self.draw_button("RETOMAR", self.play_button)
        self.draw_button("MENU", self.menu_button)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                if self.menu_button.collidepoint(mouse_pos):
                    return "menu"
                if self.play_button.collidepoint(mouse_pos):
                    return "game"

        return None


    def draw_button(self, text, rect, selected=False):
        x = rect.x
        y = rect.y

        mouse_pos = pygame.mouse.get_pos()

        hovered = rect.collidepoint(mouse_pos)

        active = hovered or selected

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
            rect,
            border_radius=4
        )

        # Borda externa
        pygame.draw.rect(
            self.screen,
            border_color,
            rect,
            width=2,
            border_radius=4
        )

        # Linha interna
        inner_rect = rect.inflate(-8, -8)

        pygame.draw.rect(
            self.screen,
            (60, 60, 40),
            inner_rect,
            width=1,
            border_radius=2
        )

        # Seta apenas no hover
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
            text,
            True,
            text_color
        )

        text_rect = label.get_rect(
            center=rect.center
        )

        self.screen.blit(label, text_rect)