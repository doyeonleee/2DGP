import random
import json
import os

from pico2d import *
from Game_Stage import Stage1
from Game_Character import Cat,Man
from Game_Heart import Heart
from Game_Obstacle import Stone, Pumpkin, Zombie

import game_framework
import title_state

name = "MainState"

cat = None
stage = None
heart = None
pumpkin = None
zombie = None
font = None

def create_objects():
    global cat, stage, heart, stone, man, pumpkin, zombie
    cat = Cat()
    stage = Stage1()
    heart = Heart()
    stone = Stone()
    pumpkin = Pumpkin()
    zombie = Zombie()
    man = Man()



def enter():
    game_framework.reset_time()
    create_objects()


def exit():
    global cat, stage, heart, stone, man, pumpkin, zombie
    del(cat)
    del(stage)
    del(heart)
    del(stone)
    del(man)
    del(pumpkin)
    del(zombie)

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
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


def collide(a,b):
    pass


def update(frame_time):
    cat.update(frame_time)
    pumpkin.update(frame_time)
    zombie.update(frame_time)

    update_canvas()


def draw_main_scene(frame_time):
    stage.draw()
    cat.draw()
    heart.draw()
    stone.draw()
    man.draw()
    pumpkin.draw()
    zombie.draw()



def draw(frame_time):
    clear_canvas()
    draw_main_scene(frame_time)
    update_canvas()





