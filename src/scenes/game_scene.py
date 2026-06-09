from game_objects.health import HealthBar
import pygame

from core.settings import Settings
from game_objects.airplane import Airplane
from game_objects.enemy import Enemy
from game_objects.boss import Boss
from components.game_button import GameButton
from utils.path_helper import resource_path


class GameScene:
    def __init__(self, screen, sound):
        self.screen = screen
        self.sound = sound
        self.settings = Settings()

        self.pause_button_rect = pygame.Rect(self.settings.WIDTH - 120, 20, 100, 50)

        self.pause_button = GameButton(self.screen, "PAUSE", self.pause_button_rect, 0)

        # ====================== GRUPOS ======================
        self.background_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.boss_group = pygame.sprite.GroupSingle()

        # ====================== BACKGROUND ======================
        self.bg = pygame.sprite.Sprite()
        try:
            background_path = resource_path("assets/images/backgrounds/background-day.png")
            self.bg.image = pygame.image.load(background_path)
            self.bg.image = pygame.transform.scale(self.bg.image,(self.settings.WIDTH, self.settings.HEIGHT))
            self.bg.rect = self.bg.image.get_rect()
            self.background_group.add(self.bg)
        except FileNotFoundError:
            print("Background 'background-day.png' não encontrado!")

        # ====================== AIRPLANE ======================
        self.airplane = Airplane((200, 200), self.bullet_group, self.sound)
        self.player_group.add(self.airplane)

        # ====================== ENEMY SPAWN ======================
        self.enemy_spawn_timer = 0
        self.enemy_spawn_delay = 90

        # ====================== BOSS SPAWN ======================

        self.boss_spawned = False
        self.boss_spawn_timer = 0
        
        # ====================== HEALTH BAR ======================

        self.health_bar = HealthBar(
            self.screen,
            self.airplane
        )


    def update(self):
        self.player_group.update()
        self.enemy_group.update()
        self.bullet_group.update()
        self.boss_group.update()

        # Spawn inimigos
        self.enemy_spawn_timer += 1

        if self.enemy_spawn_timer >= self.enemy_spawn_delay:

            enemy = Enemy(
                self.settings.WIDTH,
                self.settings.HEIGHT
            )

            self.enemy_group.add(enemy)
            self.enemy_spawn_timer = 0

        # Spawn Boss
        self.boss_spawn_timer += 1

        if (
            self.boss_spawn_timer >= 900
            and not self.boss_spawned
        ):
            boss = Boss()

            self.boss_group.add(boss)

            self.boss_spawned = True


    def draw(self):
        """Desenha tudo na tela"""
        
        self.background_group.draw(self.screen)

        self.enemy_group.draw(self.screen)

        self.boss_group.draw(self.screen)

        self.player_group.draw(self.screen)
        
        self.bullet_group.draw(self.screen)

        self.health_bar.draw()
        
        self.pause_button.draw()
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self.pause_button.rect.collidepoint(mouse_pos):
                    return "pause"
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "pause"