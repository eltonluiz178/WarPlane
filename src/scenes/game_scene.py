import pygame

from core.window import Window
from core.settings import Settings
from game_objects.airplane import Airplane

class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.window = Window(self.settings)

        # ====================== GRUPOS DE SPRITES ======================
        self.objectGroup = pygame.sprite.Group()

        # ====================== BACKGROUND ======================
        self.bg = pygame.sprite.Sprite()
        try:
            self.bg.image = pygame.image.load("assets/images/backgrounds/background-day.png")
            self.bg.image = pygame.transform.scale(self.bg.image,(self.settings.WIDTH, self.settings.HEIGHT))
            self.bg.rect = self.bg.image.get_rect()
            self.objectGroup.add(self.bg)
        except FileNotFoundError:
            print("Background 'background-day.png' não encontrado!")
        
        # ====================== AIRPLANE ======================
        self.airplane = pygame.sprite.Sprite()
        airplane = Airplane((200, 200))
        self.objectGroup.add(airplane)
        

    def update(self):
        
        self.objectGroup.update()

    def draw(self):
        """Desenha tudo na tela"""
        self.objectGroup.draw(self.window.get_surface())
        self.window.update()

    def handle_event(self, event):

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #
        #     if event.button == 1:
        #
        #         mouse_pos = pygame.mouse.get_pos()
        #
        #         if self.pause_button.collidepoint(mouse_pos):
        #             return "pause"

        return None