import pygame
import random
import time
from scenes.menu_scene import MenuScene

from core.settings import Settings
from core.window import Window

# Imports das entidades e componentes


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = Window(self.settings)
        self.clock = pygame.time.Clock()
        self.menu_scene = MenuScene(
            self.window.get_surface()
        )

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
        self.menu_scene.draw()

        self.objectGroup.draw(
            self.window.get_surface()
        )

        self.window.update()

    def run(self):
        """Game Loop principal"""
        while self.running:
            self.clock.tick(self.settings.FPS)

            self.handle_events()
            # self.update()
            self.draw()

        # Finaliza o Pygame
        pygame.quit()