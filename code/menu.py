#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect, Surface
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_F, MENU_OPTION, COLOR_B, COLOR_P, COLOR_A


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/musicmenu.wav')
        pygame.mixer_music.play(-1)
        while True:
            #textos/imagens
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(136, "Magician", (40, 150, 189), ((WIN_WIDTH / 2), 150))
            self.menu_text(136, "Shooter", COLOR_F, ((WIN_WIDTH / 2), 300))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(50, MENU_OPTION[i], COLOR_A, ((WIN_WIDTH / 2), 430 + 60 * i))
                else:
                    self.menu_text(50, MENU_OPTION[i], COLOR_B, ((WIN_WIDTH / 2), 430 + 60 * i))

            pygame.display.flip()

            #EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: #para baixo
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else :
                            menu_option = 0
                    if event.key == pygame.K_UP: #para cima
                        if menu_option > 0:
                            menu_option -= 1
                        else :
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN: #selecionando com o enter
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


