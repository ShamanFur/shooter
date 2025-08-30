#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity (entity_name:str, position=(0, 0)):
        match entity_name:
            case 'Level1bg':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'Level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH, 0)))

                bg3_left = Background('Level1bg3', (0, WIN_HEIGHT))
                bg3_left.rect.bottom = WIN_HEIGHT
                list_bg.append(bg3_left)

                bg3_right = Background('Level1bg3', (WIN_WIDTH, WIN_HEIGHT))
                bg3_right.rect.bottom = WIN_HEIGHT
                list_bg.append(bg3_right)
                return list_bg
            case 'player':
                return Player('player', (150, 470))

