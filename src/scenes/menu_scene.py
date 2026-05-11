import pygame

class MenuScene:
    def __init__(self, screen):
        self.screen = screen

        self.background = pygame.image.load(
            "assets/images/backgrounds/menu.png"
        )

        width = self.screen.get_width()
        height = self.screen.get_height()

        bg_width = self.background.get_width()
        bg_height = self.background.get_height()

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()

        scale = max(
            screen_width / bg_width,
            screen_height / bg_height
        )

        new_width = int(bg_width * scale)
        new_height = int(bg_height * scale)

        self.background = pygame.transform.scale(
            self.background,
            (new_width, new_height)
        )

        self.font = pygame.font.Font(
            "assets/fonts/press_start_regular.ttf",
            12
        )

        self.play_button = pygame.Rect(230, 240, 260, 58)

        self.config_button = pygame.Rect(230, 310, 260, 58)

        self.extras_button = pygame.Rect(230, 380, 260, 58)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                if self.play_button.collidepoint(mouse_pos):
                    return "game"

        return None

    def draw(self):
        bg_x = (self.screen.get_width() - self.background.get_width()) // 2
        bg_y = (self.screen.get_height() - self.background.get_height()) // 2

        self.screen.blit(self.background, (bg_x, bg_y))


        self.draw_button("JOGAR", self.play_button)
        self.draw_button("CONFIGURAÇÕES", self.config_button)
        self.draw_button("EXTRAS", self.extras_button)

    def draw_button(self, text, rect, selected=False):
        x = rect.x
        y = rect.y

        rect = pygame.Rect(x, y, 260, 58)

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
            center=(x + 130, y + 29)
        )

        self.screen.blit(label, text_rect)