import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        image = pygame.image.load(
            "assets/images/sprites/enemy_plane.png"
        ).convert_alpha()

        # Redimensiona
        self.image = pygame.transform.scale(
            image,
            (120, 60)
        )

        self.rect = self.image.get_rect()

        # Spawn fora da tela
        self.rect.x = screen_width + random.randint(50, 300)

        # Posição Y aleatória
        self.rect.y = random.randint(
            50,
            screen_height - self.rect.height - 50
        )

        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
