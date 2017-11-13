import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

cat = None
stage = None
heart = None
font = None



class Stage:
    def __init__(self):
        self.image = load_image('Main_BackGround.png')

    def draw(self):
        self.image.draw(500, 300)


class Heart:
    def __init__(self):
        self.image =load_image('E:\\Data\\2DGP\\Project\Resourse\\Heart_FULL.png')

    def draw(self):
        self.image.draw(900,500)


class Cat:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_IDLE, RIGHT_IDLE = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.state = self.RIGHT_IDLE

    #RUN = 8, IDLE = 10
    def update(self):
        if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
            self.frame = (self.frame +1) % 10
        elif self.state in (self.RIGHT_RUN, self.LEFT_RUN):
            self.frame = (self.frame + 1) % 8

        if self.state == self.RIGHT_RUN:
            self.x = min(1000,self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x -5)

    def draw(self):
        if self.state == self.RIGHT_IDLE:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_Right_Idle.png')
                self.image.clip_draw(self.frame * 80, 0, 80, 102, self.x, self.y)
        elif self.state == self.LEFT_IDLE:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_LEFT_Idle.png')
                self.image.clip_draw(self.frame * 80, 0, 80, 102, self.x, self.y)
        elif self.state == self.RIGHT_RUN:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_Right_RUN.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 101, self.x, self.y)
        elif self.state == self.LEFT_RUN:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_LEFT_RUN.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 101, self.x, self.y)

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
                self.state = self.LEFT_RUN
            if self.state == self.RIGHT_RUN:
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
                self.state = self.RIGHT_RUN
            if self.state == self.LEFT_RUN:
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_IDLE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_IDLE

def enter():
    global cat, stage, heart
    cat = Cat()
    stage = Stage()
    heart = Heart()


def exit():
    global cat, stage, heart
    del(cat)
    del(stage)
    del(heart)


def pause():
    pass


def resume():
    pass


def handle_events():
    global running, cat

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            cat.handle_event(event)
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
        #    game_framework.push_state(pause_state)



def update():
    cat.update()
    update_canvas()


def draw_main_scene():

    stage.draw()
    cat.draw()
    heart.draw()



def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()





