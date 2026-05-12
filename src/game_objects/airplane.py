import pygame

class Airplane(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.45

        # Configuração dos frames
        self.frame_width = 200
        self.frame_height = 100

        # Carrega spritesheet
        sprite_sheet = pygame.image.load(
            "./assets/images/sprites/airplane_sprite.png"
        ).convert_alpha()

        sheet_width = sprite_sheet.get_width()

        total_frames = sheet_width // self.frame_width

        # Corta os frames
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

    def update(self):

        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

        self.image = self.frames[int(self.current_frame)]
        
    # Para utilizar:
    # # Cria objeto animado
    # airplane = Airplane((200, 200))
    # self.objectGroup.add(airplane)
    # # # Adiciona no grupo
    # self.objectGroup.add(airplane)