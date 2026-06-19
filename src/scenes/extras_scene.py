import pygame
from core.settings import Settings
from components.game_button import GameButton
from utils.path_helper import resource_path


class ExtrasScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        background_path = resource_path("assets/images/backgrounds/menu.png")
        bg = pygame.image.load(background_path)
        scale = max(self.settings.WIDTH / bg.get_width(), self.settings.HEIGHT / bg.get_height())
        self.background = pygame.transform.scale(
            bg, (int(bg.get_width() * scale), int(bg.get_height() * scale))
        )

        self.overlay = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 160))

        font_path = resource_path("assets/fonts/press_start_regular.ttf")
        self.font_title = pygame.font.Font(font_path, 28)
        self.font_section = pygame.font.Font(font_path, 13)
        self.font_name = pygame.font.Font(font_path, 11)

        back_rect = pygame.Rect(self.settings.WIDTH - 120, 20, 100, 50)
        self.back_button = GameButton(self.screen, "VOLTAR", back_rect, 1)

        self.developers = ["Alrykemes", "Elton", "Caio", "Breno", "Arthur"]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.back_button.rect.collidepoint(pygame.mouse.get_pos()):
                    return "menu"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"
        return None

    def update(self):
        pass

    def draw(self):
        cx = self.settings.WIDTH // 2

        bg_x = (self.settings.WIDTH - self.background.get_width()) // 2
        bg_y = (self.settings.HEIGHT - self.background.get_height()) // 2
        self.screen.blit(self.background, (bg_x, bg_y))
        self.screen.blit(self.overlay, (0, 0))

        # Título
        title = self.font_title.render("CRÉDITOS", True, (255, 220, 50))
        self.screen.blit(title, title.get_rect(center=(cx, 120)))

        # Separador
        pygame.draw.line(self.screen, (255, 220, 50, 180), (cx - 240, 158), (cx + 240, 158), 2)

        # Seção de desenvolvedores
        section = self.font_section.render("Desenvolvedores", True, (200, 200, 200))
        self.screen.blit(section, section.get_rect(center=(cx, 200)))

        for i, name in enumerate(self.developers):
            text = self.font_name.render(name, True, (255, 255, 255))
            self.screen.blit(text, text.get_rect(center=(cx, 250 + i * 50)))

        self.back_button.draw()
