import pygame

from core.window import Window
from core.settings import Settings
from utils.game_button import GameButton


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

        self.play_button_rect = pygame.Rect(center[0] - button_width / 2, center[1] - button_height, 260, 58)
        self.menu_button_rect = pygame.Rect(center[0] - button_width / 2, center[1] + button_height, 260, 58)

        self.play_button = GameButton(self.screen,"RETOMAR", self.play_button_rect, 1)
        self.menu_button = GameButton(self.screen,"MENU", self.menu_button_rect, 1)

    def update(self):
        pass

    def draw(self):
        """Desenha tudo na tela"""
        self.play_button.draw()
        self.menu_button.draw()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.menu_button_rect.collidepoint(mouse_pos):
                    return "menu"
                if self.play_button_rect.collidepoint(mouse_pos):
                    return "game"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "game"

        return None