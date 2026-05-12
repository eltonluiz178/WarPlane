import pygame

from core.window import Window
from core.settings import Settings

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.window = Window(self.settings)

        self.pause_button = pygame.Rect(self.settings.WIDTH - 120, 20, 100, 50)

        self.font = pygame.font.Font(
            "assets/fonts/press_start_regular.ttf",
            12
        )

        # ====================== GRUPOS DE SPRITES ======================
        self.objectGroup = pygame.sprite.Group()

        # ====================== BACKGROUND ======================
        self.bg = pygame.sprite.Sprite()
        try:
            self.bg.image = pygame.image.load("assets/images/backgrounds/background-day.png")
            self.bg.image = pygame.transform.scale(self.bg.image,(self.settings.WIDTH, self.settings.HEIGHT))
            self.bg.rect = self.bg.image.get_rect()
            self.objectGroup.add(self.bg)
        except FileNotFoundError:
            print("Background 'background-day.png' não encontrado!")

    def draw(self):
        """Desenha tudo na tela"""
        self.objectGroup.draw(self.window.get_surface())
        self.draw_button("PAUSE", self.pause_button)
        self.window.update()  # pygame.display.update()


    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                if self.pause_button.collidepoint(mouse_pos):
                    return "pause"

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