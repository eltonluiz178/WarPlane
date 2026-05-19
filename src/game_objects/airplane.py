import pygame

class Airplane(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.45

        # ================= ANIMAÇÃO =================
        self.frame_width = 200
        self.frame_height = 100

        sprite_sheet = pygame.image.load(
            "./assets/images/sprites/airplane_sprite.png"
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

    def animate(self):

        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

        self.image = self.frames[int(self.current_frame)]

    def update(self):

        self.movement()
        self.animate()