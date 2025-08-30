#tela
import pygame

WIN_WIDTH = 1067
WIN_HEIGHT = 600
#cor
COLOR_F = (55, 145, 89)
COLOR_B = (255, 255, 255)
COLOR_P = (0, 0, 0)
COLOR_A = (255, 230, 62)

MENU_OPTION = ('STAR GAME',
               'SCORE',
               'EXIT')

EVENT_ENEMY = pygame.USEREVENT + 1

#fundo parallax
ENTITY_SPEED = {
    'Level1bg0': 1,
    'Level1bg1': 2,
    'Level1bg2': 3,
    'Level1bg3': 4,
    'Enemy': 3,
}

