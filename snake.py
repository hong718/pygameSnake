import pygame
import os
from cube import cube

width = 480
rows = 20
dis = 480 // 20



class snake():
    body = []
    turn_pos = dict()
    turn = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, colour, pos):
        self.colour = colour
        self.body.append(cube(pos))


    def move(self):
        '''
        move the snake every frame
        :return: None
        '''
        for i, c in enumerate(self.body):
            if c.pos in self.turn_pos:
                turn_dir = self.turn_pos[c.pos]
                c.dir_x, c.dir_y = turn_dir[0], turn_dir[1]
                if i == len(self.body) - 1:
                    self.turn_pos.pop(c.pos)
                c.move(c.dir_x, c.dir_y)
            else:
                if c.dir_x == 1 and c.pos[0] >= rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dir_x == -1 and c.pos[0] <= 0:
                    c.pos = (rows - 1, c.pos[1])
                elif c.dir_y == 1 and c.pos[1] >= rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dir_y == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], rows - 1)
                else:
                    c.move(c.dir_x, c.dir_y)

    def turn(self, dir):
        '''
        save the turn position and change the head's position
        :param dir: list[int]
        :return: None
        '''
        self.turn_pos[self.body[0].pos] = dir
        self.body[0].dir_x, self.body[0].dir_y = dir[0], dir[1]


    def reset(self,pos):
        '''
        reset the snake
        :param pos: tuple(int, int)
        :return: None
        '''
        self.body.clear()
        self.turn_pos.clear()
        self.body.append(cube(pos))


    def addCube(self):
        '''
        add a cube when a snack is eaten
        :return: None
        '''
        last_cube = self.body[-1]
        last_pos = last_cube.pos
        if last_cube.dir_x == 1:
            newcube_pos = (last_pos[0] - 1, last_pos[1])
            newcube = cube(newcube_pos, last_cube.dir_x, last_cube.dir_y)
            self.body.append(newcube)
        elif last_cube.dir_x == -1:
            newcube_pos = (last_pos[0] + 1, last_pos[1])
            newcube = cube(newcube_pos, last_cube.dir_x, last_cube.dir_y)
            self.body.append(newcube)
        elif last_cube.dir_y == 1:
            newcube_pos = (last_pos[0], last_pos[1] - 1)
            newcube = cube(newcube_pos, last_cube.dir_x, last_cube.dir_y)
            self.body.append(newcube)
        elif last_cube.dir_y == -1:
            newcube_pos = (last_pos[0], last_pos[1] + 1)
            newcube = cube(newcube_pos, last_cube.dir_x, last_cube.dir_y)
            self.body.append(newcube)


    def draw(self, surface):
        '''
        draw the snake cube by cube
        :param surface: surface
        :return: None
        '''
        for cube in self.body:
            cube.draw(surface)


