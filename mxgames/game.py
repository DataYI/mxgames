#!python3
# -*- coding: utf-8 -*-
'''
@name: game
@author: Memory
@date: 2018/11/20
@document: 为游戏提供一个框架的基类
'''
import pygame
from pygame.locals import *
from sys import exit

FOUR_NEIGH = {"left": (0, -1), "right": (0, 1), "up": (-1, 0), "down": (1, 0)}
EIGHT_NEIGH = list(FOUR_NEIGH.values()) + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
DIRECTION = {pygame.K_UP: "up", pygame.K_LEFT: "left", pygame.K_RIGHT: "right", pygame.K_DOWN: "down"}

# def get_index(start, end):
#     if isinstance(start, tuple) and isinstance(end, tuple):
#         return [(i, j) for i in range(*start) for j in range(*end)]
#     elif isinstance(start, tuple):
#         return [(i, j) for i in range(*start) for j in range(end)]
#     elif isinstance(end, tuple):
#         return [(i, j) for i in range(start) for j in range(*end)]
#     else:
#         return [(i, j) for i in range(start) for j in range(end)]


# class Vector(object):
#     def __init__(self, x=0.0, y=0.0):
#         self.x = x
#         self.y = y

#     def move(x, y):
        

class Game(object):
    def __init__(self, title, size, fps=30):
        self.size = size
        pygame.init()
        self.screen = pygame.display.set_mode(size, 0, 32)
        pygame.display.set_caption(title)
        self.keys = {}
        self.clicks = {}
        self.timer = pygame.time.Clock()
        self.fps = fps
        self.end = False
        self.fullscreen = False
        self.last_time = pygame.time.get_ticks()
        self.is_pause = False
        self.is_draw = True

    def bind_key(self, key, action):
        if isinstance(key, list):
            for k in key:
                self.keys[k] = action
        elif isinstance(key, int):
            self.keys[key] = action

    def bind_click(self, button, action):
        self.clicks[button] = action

    def set_fps(self, fps):
        self.fps = fps

    def handle_input(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in self.keys.keys():
                self.keys[event.key](event.key)
            if event.key == pygame.K_F11:                           # F11全屏
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN, 32)
                else:
                    self.screen = pygame.display.set_mode(self.size, 0, 32)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in self.clicks.keys():
                self.clicks[event.button](*event.pos)

    def run(self):
        while True:
            for event in pygame.event.get():
                self.handle_input(event)
            self.timer.tick(self.fps)

            self.update(pygame.time.get_ticks())
            self.draw(pygame.time.get_ticks())

    def is_end():
        return False

    def update(self, current_time):
        pass

    def draw(self, current_time):
        pass


class Test(Game):
    def __init__(self, title, size, fps=30):
        super(Test, self).__init__(title, size, fps)
        self.bind_key(pygame.K_RETURN, self.press_enter)

    def press_enter(self):
        print("press enter")

    def draw(self):
        pass


def press_space(key):
    print("press space.")


def click(x, y):
    print(x, y)


def main():
    game = Test("game", (640, 480))
    game.bind_key(pygame.K_SPACE, press_space)
    game.bind_click(1, click)
    game.run()

if __name__ == '__main__':
    main()