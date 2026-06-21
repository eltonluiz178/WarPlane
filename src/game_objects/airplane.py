import pygame
from game_objects.bullet import Bullet
from utils.path_helper import resource_path


class Airplane(pygame.sprite.Sprite):
    def __init__(self, pos, bullet_group, sound):
        super().__init__()

        self.bullet_group = bullet_group
        self.sound = sound
        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.45
        self.shoot_delay = 250
        self.last_shot = 0
        self.max_life = 250
        self.life = self.max_life

        # ================= ANIMAÇÃO =================
        self.frame_width = 200
        self.frame_height = 100

        airplane_path = resource_path("./assets/images/sprites/airplane_sprite.png")
        sprite_sheet = pygame.image.load(
            airplane_path
        ).convert_alpha()

        sheet_width = sprite_sheet.get_width()

        total_frames = sheet_width // self.frame_width

        for i in range(total_frames):

            frame = sprite_sheet.subsurface(
                (
                    i * self.frame_width,
                    0,
                    self.frame_width,
                    self.frame_height
                )
            )

            self.frames.append(frame)

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=pos)

        # ================= MOVIMENTO =================
        self.speed = 5

    def movement(self):

        keys = pygame.key.get_pressed()

        # Esquerda
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        # Direita
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Cima
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed

        # Baixo
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > 1280:
            self.rect.right = 1280

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > 720:
            self.rect.bottom = 720

    def attack(self):

        keys = pygame.key.get_pressed()

        current_time = pygame.time.get_ticks()

        if keys[pygame.K_SPACE]:

            if current_time - self.last_shot > self.shoot_delay:

                bullet = Bullet(
                    (
                        self.rect.right - 15,
                        self.rect.centery + 10
                    )
                )

                self.bullet_group.add(bullet)

                self.sound.play_sfx("shot", 0)

                self.last_shot = current_time

    def take_damage(self, damage):

        self.life -= damage

        if self.life <= 0:
            self.life = 0
            self.die()

    def heal(self, amount):

        self.life += amount

        if self.life > self.max_life:
            self.life = self.max_life

    def die(self):
        self.kill()

    def animate(self):

        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

        self.image = self.frames[int(self.current_frame)]

    def update(self):

        self.movement()
        self.animate()
        self.attack()
