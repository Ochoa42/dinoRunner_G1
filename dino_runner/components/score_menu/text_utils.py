import pygame
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
black_color = (0,0,0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 20)
    text = font.render('Points: '+str(points),True, black_color)
