import pygame

from utils.game_button import GameButton


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

        self.play_button_rect = pygame.Rect(320, 310, 260, 58)
        self.config_button_rect = pygame.Rect(320, 380, 260, 58)
        self.extras_button_rect = pygame.Rect(320, 450, 260, 58)

        self.play_button = GameButton(self.screen, "JOGAR", self.play_button_rect, 1)
        self.config_button = GameButton(self.screen, "CONFIGURAÇÕES", self.config_button_rect, 1)
        self.extras_button = GameButton(self.screen, "EXTRAS", self.extras_button_rect, 1)

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                mouse_pos = pygame.mouse.get_pos()

                if self.play_button.rect.collidepoint(mouse_pos):
                    return "game"

        return None

    def update(self):
        
        pass

    def draw(self):
        bg_x = (self.screen.get_width() - self.background.get_width()) // 2
        bg_y = (self.screen.get_height() - self.background.get_height()) // 2

        self.screen.blit(self.background, (bg_x, bg_y))

        self.play_button.draw()
        self.config_button.draw()
        self.extras_button.draw()
