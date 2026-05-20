import pygame
from utils.path_helper import resource_path


class SoundManager:
    def __init__(self):
        pygame.mixer.init()

        # Registro de músicas por cena
        self._tracks = {
            "menu": resource_path("assets/sounds/musics/boss_opening_music.mp3"),
            "boss": resource_path("assets/sounds/musics/boss_opening_music.mp3"),
            "game": resource_path("assets/sounds/musics/music_game.mp3"),
        }

        self.sfx = {
            "airplane": pygame.mixer.Sound(resource_path("assets/sounds/sfx/airplane.mp3")),
            "shot": pygame.mixer.Sound(resource_path("assets/sounds/sfx/shot.mp3")),
        }

        self._current_scene = None
        self._volume = 0.05

        self.sfx["airplane"].set_volume(0.2)
        self.sfx["shot"].set_volume(0.4)

    def on_scene_change(self, scene_name: str):

        if scene_name == self._current_scene:
            return  # mesma cena, não faz nada

        if scene_name in self._tracks:
            self._play(scene_name)
        else:
            # Cena sem música: pausa o que estiver tocando
            self._pause()

        if scene_name == "game":
            self.play_airplane()
        else:
            self.stop_airplane()

        self._current_scene = scene_name

    def set_volume(self, volume: float):
        self._volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self._volume)

    def pause(self):
        self._pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def _play(self, scene_name: str):
        track_path = self._tracks[scene_name]

        if self._current_scene == scene_name and pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
            return

        pygame.mixer.music.stop()
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.set_volume(self._volume)
        pygame.mixer.music.play(-1)  # -1 = loop infinito

    def _pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    
    def play_airplane(self):
        self.sfx["airplane"].play(-1)

    def stop_airplane(self):
        self.sfx["airplane"].stop()

    def play_shot(self):
        self.sfx["shot"].play()