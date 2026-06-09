import pygame

from utils.path_helper import resource_path


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):

        super().__init__()

        # ================= IMAGE =================

        bullet_path = resource_path("./assets/images/sprites/bullet_silver.png")
        self.image = pygame.image.load(
            bullet_path
        ).convert_alpha()

        # Escala opcional
        self.image = pygame.transform.scale(
            self.image,
            (24, 12)
        )

        # ================= RECT =================

        self.rect = self.image.get_rect(
            center=pos
        )

        # ================= MOVEMENT =================

        self.speed = 14

    def update(self):

        self.rect.x += self.speed

        # Remove quando sair da tela
        if self.rect.left > 1280:
            self.kill()