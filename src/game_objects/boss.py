import pygame

from utils.path_helper import resource_path


class Boss(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        boss_path = resource_path("assets/images/sprites/boss_juggernaut.png")
        self.image = pygame.image.load(
            boss_path
        ).convert_alpha()

        self.rect = self.image.get_rect()

        # Começa totalmente fora da tela
        self.rect.x = 1400
        self.rect.y = 200

        self.speed = 2

    def update(self):

        # Entra lentamente
        if self.rect.x > 700:
            self.rect.x -= self.speed