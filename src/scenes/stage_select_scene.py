import pygame

from components.game_button import GameButton
from core.settings import Settings
from utils.path_helper import resource_path


class StageSelectScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()

        self.stages = [
            {
                "id": "day",
                "name": "DIA",
                "icon": "assets/images/icons/day-phase-icon.png",
                "background": "assets/images/backgrounds/background-day.png",
            },
            {
                "id": "night",
                "name": "NOITE",
                "icon": "assets/images/icons/night-phase-icon.png",
                "background": "assets/images/backgrounds/background-night.png",
            },
            {
                "id": "snow",
                "name": "NEVE",
                "icon": "assets/images/icons/snow-phase-icon.png",
                "background": "assets/images/backgrounds/background-snow.png",
            },
        ]

        self.selected_stage_id = "day"
        self.menu_background = self._load_background("assets/images/backgrounds/menu.png")
        self.stage_icons = {}

        for stage in self.stages:
            self.stage_icons[stage["id"]] = self._load_icon(stage["icon"])

        font_path = resource_path("assets/fonts/press_start_regular.ttf")
        self.title_font = pygame.font.Font(font_path, 28)
        self.phase_name_font = pygame.font.Font(font_path, 12)

        self.stage_buttons = []
        card_width = 200
        card_height = 240
        start_x = 200
        start_y = 150
        spacing = 360

        for index, stage in enumerate(self.stages):
            rect = pygame.Rect(start_x + (index * spacing), start_y, card_width, card_height)
            button = GameButton(self.screen, "", rect, 0)
            self.stage_buttons.append((stage, rect, button))

        self.back_button_rect = pygame.Rect(350, 530, 240, 50)
        self.start_button_rect = pygame.Rect(690, 530, 240, 50)
        self.back_button = GameButton(self.screen, "VOLTAR", self.back_button_rect, 0)
        self.start_button = GameButton(self.screen, "COMEÇAR", self.start_button_rect, 0)

    def _load_background(self, background_path):
        path = resource_path(background_path)
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (self.settings.WIDTH, self.settings.HEIGHT))
        return image

    def _load_icon(self, icon_path):
        path = resource_path(icon_path)
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (100, 100))
        return image

    def handle_event(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return None

        mouse_pos = pygame.mouse.get_pos()

        for stage, rect, button in self.stage_buttons:
            if button.rect.collidepoint(mouse_pos):
                self.selected_stage_id = stage["id"]
                return None

        if self.back_button.rect.collidepoint(mouse_pos):
            return "menu"

        if self.start_button.rect.collidepoint(mouse_pos):
            return ("start_game", self.selected_stage_id)

        return None

    def update(self):
        return None

    def draw(self):
        self.screen.blit(self.menu_background, (0, 0))

        overlay = pygame.Surface((self.settings.WIDTH, self.settings.HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 80))
        self.screen.blit(overlay, (0, 0))

        title = self.title_font.render("ESCOLHA A FASE", True, (255, 220, 90))
        title_rect = title.get_rect(center=(self.settings.WIDTH // 2, 80))
        self.screen.blit(title, title_rect)

        for stage, rect, button in self.stage_buttons:
            button.selected = stage["id"] == self.selected_stage_id
            button.draw()

            icon = self.stage_icons[stage["id"]]
            icon_rect = icon.get_rect(center=(rect.centerx, rect.y + 70))
            self.screen.blit(icon, icon_rect)

            phase_name = self.phase_name_font.render(stage["name"], True, (255, 255, 255))
            name_rect = phase_name.get_rect(center=(rect.centerx, rect.bottom - 20))
            self.screen.blit(phase_name, name_rect)

        self.back_button.draw()
        self.start_button.draw()
