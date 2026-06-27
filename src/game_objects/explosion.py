import pygame
from utils.path_helper import resource_path


class Explosion(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.frames = []

        # Carrega frames da explosão
        i = 1
        while True:
            path = resource_path(
                f"assets/images/effects/explosion_{i:02d}.png"
            )

            try:
                img = pygame.image.load(path).convert_alpha()
            except FileNotFoundError:
                break

            img = pygame.transform.scale(img, (120, 120))
            self.frames.append(img)
            i += 1

        if len(self.frames) == 0:
            raise ValueError("Nenhuma imagem de explosão foi encontrada!")

        self.frame_index = 0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

        self.animation_speed = 3
        self.counter = 0

    def update(self):

        self.counter += 1

        if self.counter >= self.animation_speed:
            self.counter = 0
            self.frame_index += 1

            if self.frame_index >= len(self.frames):
                self.kill()
            else:
                self.image = self.frames[self.frame_index]