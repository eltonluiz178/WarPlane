import pygame
from core.settings import Settings
from utils.path_helper import resource_path


class PhaseCompleteScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        background_path = resource_path("assets/images/backgrounds/menu.png")
        bg = pygame.image.load(background_path)
        self.background = pygame.transform.scale(bg, (self.settings.WIDTH, self.settings.HEIGHT))

        font_path = resource_path("assets/fonts/press_start_regular.ttf")
        self.title_font = pygame.font.Font(font_path, 48)
        self.subtitle_font = pygame.font.Font(font_path, 20)

        self.overlay = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 180))

        self._elapsed = 0.0
        self._duration = 3.0

    def reset(self):
        self._elapsed = 0.0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            return "phase_complete"
        return None

    def update(self):
        dt = 1.0 / self.settings.FPS
        self._elapsed += dt

        if self._elapsed >= self._duration:
            return "phase_complete"
        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.overlay, (0, 0))

        cx = self.settings.WIDTH // 2
        cy = self.settings.HEIGHT // 2

        title = self.title_font.render("FASE CONCLUÍDA!", True, (50, 255, 120))
        title_rect = title.get_rect(center=(cx, cy - 80))
        self.screen.blit(title, title_rect)

        subtitle = self.subtitle_font.render("Clique ou pressione uma tecla para continuar", True, (255, 255, 255))
        subtitle_rect = subtitle.get_rect(center=(cx, cy + 80))
        self.screen.blit(subtitle, subtitle_rect)

        progress = int((self._elapsed / self._duration) * 100)
        progress_text = self.subtitle_font.render(f"Voltando em {int(self._duration - self._elapsed)}s", True, (255, 220, 90))
        progress_rect = progress_text.get_rect(center=(cx, cy + 150))
        self.screen.blit(progress_text, progress_rect)
