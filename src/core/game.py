import pygame
import random
import time

from managers.sound_manager import SoundManager
from scenes.config_scene import ConfigScene
from scenes.menu_scene import MenuScene
from scenes.game_scene import GameScene
from scenes.pause_scene import PauseScene
from scenes.countdown_scene import CountdownScene
from core.settings import Settings
from core.window import Window
from utils.path_helper import resource_path


class Game:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = Window(self.settings)
        self.clock = pygame.time.Clock()
        self.sound = SoundManager()

        # ====================== ICON ======================

        game_icon_path = resource_path("assets/images/icons/game-icon.png")
        icon = pygame.image.load(game_icon_path)
        pygame.display.set_icon(icon)

        self.settings = Settings()
        self.window = Window(self.settings)
        self.clock = pygame.time.Clock()
        self.sound = SoundManager()

        # ====================== SCENES ======================
        self.menu_scene = MenuScene(
            self.window.get_surface()
        )
        self.game_scene = GameScene(
            self.window.get_surface(),
            self.sound
        )
        self.pause_scene = PauseScene(
            self.window.get_surface()
        )
        self.config_scene = ConfigScene(
            self.window.get_surface(),
            self.sound
        )
        self.countdown_scene = CountdownScene(
            self.window.get_surface()
        )

        self.current_scene = self.menu_scene
        self.sound.on_scene_change("menu")
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            result = self.current_scene.handle_event(event)

            if result == "game":
                self.countdown_scene.reset()
                self.current_scene = self.countdown_scene
                self.sound.on_scene_change("game")
            if result == "menu":
                self.current_scene = self.menu_scene
                self.sound.on_scene_change("menu")
            if result == "pause":
                self.current_scene = self.pause_scene
            if result == "config":
                self.current_scene = self.config_scene

    def update(self):
        result = self.current_scene.update()
        if result == "game":
            self.current_scene = self.game_scene

    def draw(self):
        # Limpa a tela
        self.window.get_surface().fill((0, 0, 0))
        # Desenha cena atual
        self.current_scene.draw()
        # Atualiza janela
        self.window.update()

    def run(self):
        while self.running:
            # Limita FPS
            self.clock.tick(self.settings.FPS)
            # Eventos
            self.handle_events()
            # Atualizações
            self.update()
            # Renderização
            self.draw()

        pygame.quit()
