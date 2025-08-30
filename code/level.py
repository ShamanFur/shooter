#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import WIN_WIDTH, COLOR_B, WIN_HEIGHT, EVENT_ENEMY


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list [Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))
        player = EntityFactory.get_entity('player')
        self.entity_list.append(player)
        self.timeout = 30000 #30 segundos
        pygame.time.set_timer(EVENT_ENEMY, 5000)

    def run(self):
        pygame.mixer_music.load(f'./assets/jogo.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
            for entity in self.entity_list:
                entity.move()
                #arrumando o parallax
            self.window.fill((0, 0, 0))
            for entity in self.entity_list:
                self.window.blit(entity.surf, entity.rect)



            self.level_text(30, f'{self.name} - TimeOut:{self.timeout / 1000:.1f}s', COLOR_B, (55, 25))
            self.level_text(20, f'fps:{clock.get_fps():.0f}', COLOR_B, (45, 580))
            self.level_text(20, f'entidades:{len(self.entity_list)}', COLOR_B, (150, 580))
            pygame.display.flip()
            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans MS", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


