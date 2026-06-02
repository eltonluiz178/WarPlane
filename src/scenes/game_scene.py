import pygame

from core.settings import Settings
from game_objects.airplane import Airplane
from game_objects.enemy import Enemy
from game_objects.boss import Boss
from components.game_button import GameButton

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
            self.bg.image = pygame.image.load("assets/images/backgrounds/background-day.png")
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

        return None


    def draw_button(self, text, rect, selected=False):
        x = rect.x
        y = rect.y

        mouse_pos = pygame.mouse.get_pos()
        hovered = rect.collidepoint(mouse_pos)
        active = hovered or selected

        # Cores
        if active:
            bg_color = (168, 78, 18)
            border_color = (255, 170, 70)
            text_color = (255, 245, 220)
            arrow_color = (255, 140, 0)
        else:
            bg_color = (18, 18, 18)
            border_color = (90, 90, 50)
            text_color = (230, 230, 230)

        # Fundo principal
        pygame.draw.rect(
            self.screen,
            bg_color,
            rect,
            border_radius=4
        )

        # Borda externa
        pygame.draw.rect(
            self.screen,
            border_color,
            rect,
            width=2,
            border_radius=4
        )

        # Linha interna
        inner_rect = rect.inflate(-8, -8)

        pygame.draw.rect(
            self.screen,
            (60, 60, 40),
            inner_rect,
            width=1,
            border_radius=2
        )

        # Texto
        label = self.font.render(
            text,
            True,
            text_color
        )

        text_rect = label.get_rect(
            center=rect.center
        )

        self.screen.blit(label, text_rect)
