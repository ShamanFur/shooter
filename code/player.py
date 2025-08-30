#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Entity import Entity
from code.const import WIN_HEIGHT


class Player(Entity):

    def __init__(self, name:str, position:tuple):
        super().__init__(name, position)
        self.vel_vertical = 0
        self.gravidade = 1
        self.pulo = -15
        #pulo duplo (juro sao 2 da manha tentei muito colocar o pulo duplo mas n deu n dps volto aqui)
        self.max_jumps = 2
        self.jumps_done = 0
        self.rect.topleft = position

    def move(self):
        keys = pygame.key.get_pressed()
        self.vel_vertical += self.gravidade
        self.rect.y += self.vel_vertical

        # chão
        ground = WIN_HEIGHT - self.rect.height - 20
        if self.rect.y >= ground:
            self.rect.y = ground
            self.vel_vertical = 0
            self.jumps_done = 0  # reset quando toca o chão
            
        # pulo
        if keys[pygame.K_UP] and self.jumps_done < self.max_jumps:
            self.vel_vertical = self.pulo
            self.jumps_done += 1
