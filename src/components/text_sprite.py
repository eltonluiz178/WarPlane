import pygame

from utils.path_helper import resource_path


class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font_size, color, textRect, *groups):
        super().__init__(*groups)
        # Cria a fonte
        font_path = resource_path("assets/fonts/press_start_regular.ttf")
        self.font = pygame.font.Font(font_path,font_size)
        self.color = color
        self.update_text(text)
        self.rect = textRect

    def update_text(self, new_text):
        """Atualiza o texto e recria a imagem do sprite"""
        self.image = self.font.render(new_text, True, self.color)