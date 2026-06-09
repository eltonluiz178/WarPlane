import pygame

class HealthBar:

    def __init__(self, screen, player):

        self.screen = screen
        self.player = player

        self.max_life = player.life

        self.x = 20
        self.y = 20

        self.width = 300
        self.height = 25

    def draw(self):

        # Fundo
        pygame.draw.rect(
            self.screen,
            (60, 60, 60),
            (self.x, self.y, self.width, self.height)
        )

        # Vida atual
        current_width = (
            self.player.life /
            self.player.max_life
        ) * self.width

        pygame.draw.rect(
            self.screen,
            (50, 220, 50),
            (self.x, self.y, current_width, self.height)
        )

        # Borda
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (self.x, self.y, self.width, self.height),
            2
        )