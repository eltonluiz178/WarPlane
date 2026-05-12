import pygame
import random
import time
from scenes.menu_scene import MenuScene
from scenes.game_scene import GameScene
from scenes.pause_scene import PauseScene

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
        self.game_scene = GameScene(
            self.window.get_surface()
        )
        self.pause_scene = PauseScene(
            self.window.get_surface()
        )

        self.current_scene = self.menu_scene

        self.running = True

    def handle_events(self):
        """Gerencia eventos do jogo (fechar janela, etc.)"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            result = self.current_scene.handle_event(event)

            if result == "game":
                self.current_scene = self.game_scene
            if result == "menu":
                self.current_scene = self.menu_scene
            if result == "pause":
                self.current_scene = self.pause_scene


    def draw(self):
        self.current_scene.draw()
        self.window.update()

    def run(self):
        """Game Loop principal"""
        while self.running:
            self.clock.tick(self.settings.FPS)

            self.handle_events()
            self.draw()

        # Finaliza o Pygame
        pygame.quit()