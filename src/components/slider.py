import pygame

from components.text_sprite import TextSprite


class Slider:
    def __init__(self, screen, text_slider, x, y, slider_width, valor_inicial=1.0):
        self.screen = screen
        self.trilha = pygame.Rect(x, y, slider_width, 8)
        self.thumb = pygame.Rect(x, y - 8, 16, 24)
        self.text_slider = text_slider
        self.arrastando = False

        self.text = TextSprite(text_slider, 12, (230, 230, 230), pygame.Rect(0, 0, 0, 0))

        # Centraliza o texto acima da trilha
        texto_x = self.trilha.centerx - self.text.image.get_width() // 2
        texto_y = self.trilha.y - self.text.image.get_height() - 10  # 10px acima da trilha
        self.text_rect = pygame.Rect(texto_x, texto_y, self.text.image.get_width(), self.text.image.get_height())

        # Posiciona o thumb de acordo com o valor inicial
        self.set_valor(valor_inicial)

    def set_valor(self, valor):
        valor = max(0.0, min(1.0, valor))  # clamp do valor
        intervalo = self.trilha.width - self.thumb.width
        self.thumb.x = self.trilha.x + int(valor * intervalo)

    def valor(self):
        intervalo = self.trilha.width - self.thumb.width
        return (self.thumb.x - self.trilha.x) / intervalo

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.thumb.collidepoint(event.pos):
                self.arrastando = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.arrastando = False
        if event.type == pygame.MOUSEMOTION and self.arrastando:
            novo_x = event.pos[0] - self.thumb.width // 2
            novo_x = max(self.trilha.x, min(novo_x, self.trilha.x + self.trilha.width - self.thumb.width))
            self.thumb.x = novo_x

    def draw(self):
        pygame.draw.rect(self.screen, (80, 80, 80), self.trilha)
        pygame.draw.rect(self.screen, (255, 255, 255), self.thumb)

        self.screen.blit(self.text.image, self.text_rect)