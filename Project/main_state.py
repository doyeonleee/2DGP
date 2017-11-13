import random
import json
import os

from pico2d import *
from Game_Stage import Stage1
from Game_Character import Cat
from Game_Heart import Heart
from Game_Obstacle import Stone

import game_framework
import title_state

name = "MainState"

cat = None
stage = None
heart = None
font = None


def enter():
    global cat, stage, heart, stone
    cat = Cat()
    stage = Stage1()
    heart = Heart()
    stone = Stone()


def exit():
    global cat, stage, heart, stone
    del(cat)
    del(stage)
    del(heart)
    del(stone)

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
    stone.draw()



def draw():
    clear_canvas()
    draw_main_scene()
    update_canvas()





