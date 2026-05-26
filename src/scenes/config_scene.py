import pygame

from core.settings import Settings
from core.window import Window
from components.game_button import GameButton
from components.slider import Slider


class ConfigScene:
    def __init__(self, screen, sound):
        self.screen = screen
        self.sound = sound
        self.settings = Settings()
        self.Window = Window(self.settings)

        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        center = (screen_width // 2, screen_height // 2)
        slider_width = 260
        slider_height = 60

        x = center[0] - slider_width / 2

        self.sliderSound = Slider(self.screen, "Efeitos Sonoros", x, center[1] - slider_height, slider_width, 0.05)
        self.sliderMusic = Slider(self.screen, "Música", x, center[1] + slider_height, slider_width, 0.05)

        self.back_button_rect = pygame.Rect(self.settings.WIDTH - 120, 20, 100, 50)

        self.back_button = GameButton(self.screen, "VOLTAR", self.back_button_rect, 1)

    def update(self):
        pass

        self.sound.set_volume_effects(self.sliderSound.valor())
        self.sound.set_volume_music(self.sliderMusic.valor())

    def draw(self):
        """Desenha tudo na tela"""
        self.sliderSound.draw()
        self.sliderMusic.draw()

        self.back_button.draw()

    def handle_event(self, event):
        self.sliderSound.handle_event(event)
        self.sliderMusic.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.back_button_rect.collidepoint(mouse_pos):
                    return "menu"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"

        return None