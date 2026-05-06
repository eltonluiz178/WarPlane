import pygame
import random
import time

from core.settings import Settings
from core.window import Window

# Imports das entidades e componentes


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = Window(self.settings)
        self.clock = pygame.time.Clock()

        self.objectGroup = pygame.sprite.Group()

        self.running = True

    def handle_events(self):
        """Gerencia eventos do jogo (fechar janela, etc.)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        test = 'teste'


    def draw(self):
        """Desenha tudo na tela"""
        self.objectGroup.draw(self.window.get_surface())
        self.window.update()  # pygame.display.update()

    def run(self):
        """Game Loop principal"""
        while self.running:
            self.clock.tick(self.settings.FPS)

            self.handle_events()
            # self.update()
            self.draw()

        # Finaliza o Pygame
        pygame.quit()