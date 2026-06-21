import pygame
from core.settings import Settings
from utils.path_helper import resource_path


class CountdownScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        background_path = resource_path("assets/images/backgrounds/background-day.png")
        bg = pygame.image.load(background_path)
        self.background = pygame.transform.scale(bg, (self.settings.WIDTH, self.settings.HEIGHT))

        font_path = resource_path("assets/fonts/press_start_regular.ttf")
        self.font_number = pygame.font.Font(font_path, 120)
        self.font_start = pygame.font.Font(font_path, 48)

        self.overlay = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 120))

        self._elapsed = 0.0
        self._done = False

        # Durações em segundos: 3 → 2 → 1 (1s cada) + "Começar!" (0.8s)
        self._steps = [
            (1.0, "3", self.font_number),
            (1.0, "2", self.font_number),
            (1.0, "1", self.font_number),
            (0.8, "Começar!", self.font_start),
        ]
        self._total = sum(d for d, *_ in self._steps)

    def reset(self):
        self._elapsed = 0.0
        self._done = False

    def _current_label(self):
        acc = 0.0
        for duration, label, font in self._steps:
            acc += duration
            if self._elapsed < acc:
                return label, font
        return None, None

    def handle_event(self, event):
        return None

    def update(self):
        dt = 1.0 / self.settings.FPS
        self._elapsed += dt

        if self._elapsed >= self._total:
            self._done = True
            return "game"
        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.overlay, (0, 0))

        label, font = self._current_label()
        if label is None:
            return

        cx = self.settings.WIDTH // 2
        cy = self.settings.HEIGHT // 2

        # Sombra
        shadow = font.render(label, True, (0, 0, 0))
        shadow_rect = shadow.get_rect(center=(cx + 4, cy + 4))
        self.screen.blit(shadow, shadow_rect)

        # Texto principal
        color = (255, 220, 50) if label.isdigit() else (50, 255, 120)
        text = font.render(label, True, color)
        text_rect = text.get_rect(center=(cx, cy))
        self.screen.blit(text, text_rect)
