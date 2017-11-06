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
        self.image =load_image('C:\\Users\\소연\\Desktop\\2D_project\\2DGP\Project\\Resourse\\Heart_FULL.png')

    def draw(self):
        self.image.draw(900,500)


class Cat:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.right_image = load_image('C:\\Users\\소연\\Desktop\\2D_project\\2DGP\Project\\Resourse\\Cat_Right_Walk.png')
        self.left_image = load_image('C:\\Users\\소연\\Desktop\\2D_project\\2DGP\Project\\Resourse\\Cat_Left_Walk.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += self.dir
        if self.x >= 1000:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1


    def draw(self):
        if self.dir > 0:
            self.right_image.clip_draw(self.frame * 102, 0, 100, 100, self.x, self.y)
        elif self.dir < 0:
            self.left_image.clip_draw(self.frame * 102, 0, 100, 100, self.x, self.y)
        #delay(0.01)




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
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
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





