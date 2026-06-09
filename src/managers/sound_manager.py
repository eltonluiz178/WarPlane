import pygame
from utils.path_helper import resource_path
from pathlib import Path


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        sound_path = BASE_DIR / "assets" / "sounds"

        # Registro de músicas por cena
        self._tracks = {
            "menu": resource_path(sound_path / "musics" / "boss_opening_music.mp3"),
            "boss": resource_path(sound_path / "musics" / "boss_opening_music.mp3"),
            "game": resource_path(sound_path / "musics" / "music_game.mp3"),
        }

        self.sfx = {
            "airplane": pygame.mixer.Sound(resource_path(sound_path / "sfx" / "airplane.mp3")),
            "shot": pygame.mixer.Sound(resource_path(sound_path / "sfx" / "shot.mp3")),
        }

        self._current_scene = None
        self._volume_music = 0.05
        self._volume_effects = 0.05

        self.set_volume_music(self._volume_music)
        self.set_volume_effects(self._volume_effects)

    def on_scene_change(self, scene_name: str):

        if scene_name == self._current_scene:
            return  # mesma cena, não faz nada

        if scene_name in self._tracks:
            self._play(scene_name)
        else:
            # Cena sem música: pausa o que estiver tocando
            self._pause()

        if scene_name == "game":
            self.play_sfx("airplane", 1)
        else:
            self.stop_sfx("airplane")

        self._current_scene = scene_name

    def set_volume_music(self, volume: float):
        self._volume_music = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self._volume_music)

    def set_volume_effects(self, volume: float):
        self._volume_effects = max(0.0, min(1.0, volume))
        for sfx in self.sfx.values():
            sfx.set_volume(self._volume_effects)

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
        pygame.mixer.music.set_volume(self._volume_music)
        pygame.mixer.music.play(-1)  # -1 = loop infinito

    def _pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def play_sfx(self, sound_name, loop):
        loops = -1 if loop else 0
        self.sfx[sound_name].play(loops)

    def stop_sfx(self, sound_name):
        self.sfx[sound_name].stop()