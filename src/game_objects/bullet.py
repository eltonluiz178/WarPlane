import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, pos):

        super().__init__()

        # ================= IMAGE =================

        self.image = pygame.image.load(
            "./assets/images/sprites/bullet_silver.png"
        ).convert_alpha()

        # Escala opcional
        self.image = pygame.transform.scale(
            self.image,
            (32, 16)
        )

        # ================= RECT =================

        self.rect = self.image.get_rect(
            center=pos
        )

        # ================= MOVEMENT =================

        self.speed = 12

    def update(self):

        self.rect.x += self.speed

        # Remove quando sair da tela
        if self.rect.left > 1280:
            self.kill()