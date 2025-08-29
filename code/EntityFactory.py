#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background


class EntityFactory:

    def get_entity(entity_name:str, position = (0, 0)):
        match entity_name:
            case 'levelbg1':
                list_bg = []
                for i in range(3):
                    list_bg.append(Background(f'levelbg{i}', position(0, 0)))
