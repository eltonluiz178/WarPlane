from game_objects.health import HealthBar
import pygame

from core.settings import Settings
from game_objects.airplane import Airplane
from game_objects.explosion import Explosion
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
        self.explosion_group = pygame.sprite.Group()
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
        self.boss_health_bar = None

        # ====================== HEALTH BAR ======================

        self.health_bar = HealthBar(
            self.screen,
            self.airplane
        )


    def update(self):
        self.player_group.update()
        self.enemy_group.update()
        self.bullet_group.update()
        self.explosion_group.update()
        self.boss_group.update()

       # ================= COLISÕES =================

        # 1. Bala x Inimigo
        hits = pygame.sprite.groupcollide(
            self.bullet_group,
            self.enemy_group,
            True,   # remove bala
            True    # remove inimigo
        )

        # 2. Avião x Inimigo
        player_hits = pygame.sprite.spritecollide(
            self.airplane,
            self.enemy_group,
            True # Remove o inimigo ao bater
        )

        for enemy in hits:
            explosion = Explosion(*enemy.rect.center)
            self.explosion_group.add(explosion)
            enemy.kill()

        for hit in player_hits:
            self.airplane.take_damage(50)  # Dano causado por um inimigo comum
            if self.airplane.life <= 0:
                print("GAME OVER - Avião Destruído")


        # 3. Bala x Boss
        boss_hits = pygame.sprite.groupcollide(
            self.bullet_group,
            self.boss_group,
            True,   # remove bala
            False   # não remove o boss instantaneamente
        )

        # Aplica dano ao Boss para cada bala que bater
        for bullet, bosses in boss_hits.items():
            for b in bosses:
                b.take_damage(25) # Valor do dano da bala
                print(f"Boss atingido! Vida: {b.life}")

        # 4. Avião x Boss
        if pygame.sprite.spritecollide(self.airplane, self.boss_group, False):
            # Aplica dano  contínuo por frame
            self.airplane.take_damage(2)
            if self.airplane.life <= 0:
                print("GAME OVER - Avião Esmagado pelo Boss")

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

        if self.boss_spawn_timer >= 900 and not self.boss_spawned:
            boss = Boss()
            self.boss_group.add(boss)
            self.boss_spawned = True

            # Cria a barra de vida do Boss centralizada no topo e vermelha
            self.boss_health_bar = HealthBar(
                self.screen,
                boss,
                x=(self.settings.WIDTH // 2) - 150, # Centraliza
                y=20,
                color=(220, 50, 50) # Vermelho
            )

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
        self.explosion_group.draw(self.screen)
        self.health_bar.draw()

        # Desenha a barra do boss só se ele existir e ainda tiver vida
        if self.boss_health_bar and self.boss_group.sprite:
            self.boss_health_bar.draw()

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
