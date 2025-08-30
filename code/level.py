#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list [Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1bg'))

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            #arrumando efeito parallax
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            for entity in self.entity_list:
                entity.move()
            self.window.fill((0, 0, 0))
            for entity in self.entity_list:
                self.window.blit(source= entity.surf, dest= entity.rect)
            pygame.display.flip()
            clock.tick(60)

