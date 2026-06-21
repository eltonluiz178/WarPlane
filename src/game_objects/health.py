import pygame

class HealthBar:
    # Adicionamos x, y e color como opcionais
    def __init__(self, screen, entity, x=20, y=20, color=(50, 220, 50)):
        self.screen = screen
        self.entity = entity # Mudamos o nome de player para entity (entidade)
        self.max_life = entity.max_life

        self.x = x
        self.y = y
        self.width = 300
        self.height = 25
        self.color = color

    def draw(self):
        # Fundo
        pygame.draw.rect(
            self.screen,
            (60, 60, 60),
            (self.x, self.y, self.width, self.height)
        )

        # Vida atual
        current_width = (self.entity.life / self.entity.max_life) * self.width

        # Cor dinâmica baseada no que foi passado no __init__
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x, self.y, current_width, self.height)
        )

        # Borda
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (self.x, self.y, self.width, self.height),
            2
        )
