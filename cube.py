import pygame
import os

width = 480
rows = 20



class cube():
    def __init__(self, pos, dir_x = -1, dir_y = 0, colour = (255, 0, 0)):
        self.pos = pos
        self.dis = width // rows
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.colour = colour

    def move(self,dir_x, dir_y):
        '''
        move a cube every frame
        :param dir_x: int
        :param dir_y: int
        :return: None
        '''
        self.pos = (self.pos[0] + dir_x, self.pos[1] + dir_y)



    def draw(self, surface):
        '''
        draw a cube
        :param surface: surface
        :return: None
        '''
        pygame.draw.rect(surface, self.colour, (self.pos[0] * self.dis, self.pos[1] * self.dis, self.dis, self.dis))

