import pygame
from pygame.mixer import mixer_music

class MusicaFondo:

    def __init__(self):
      self.sound_background = pygame.mixer.Sound("dino_runner/assets/music_background/music.mp3")  
      self.off = pygame.mixer.Sound.stop
      self.play = pygame.mixer.Sound.play
      

