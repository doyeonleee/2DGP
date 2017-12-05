import random
import json
import os

import game_framework
import gameover_state
import title_state
import pause_state
import stageclear_state

from pico2d import *
from collision import *

from Stage import Stage as Background
from Stage import Land as Land
from Life import Heart as Heart
from Character import Cat as Cat
from Character import Man as Man

from global_values import window_height, window_width

name = "main_state"

stage = None
cat = None
man = None
lands = None
heart = None

def create_objects():
    global stage, cat, lands, man, heart
    stage = Background()
    cat = Cat()
    heart = Heart()
    lands = Land(stage)
    man = Man(stage)

    stage.set_center_object(cat)
    cat.set_background(stage)

def delete_objects():
    global stage, cat, lands, man, heart
    del(stage)
    del(cat)
    del(lands)
    del(man)
    del(heart)

def enter():
    open_canvas(window_width, window_height)
    game_framework.reset_time()
    create_objects()

def exit():
    delete_objects()
    close_canvas()

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            cat.handle_event(event)

def update(frame_time):
    stage.update(frame_time)
    cat.update(frame_time)
    lands.update(frame_time)
    man.update(frame_time)
    update_canvas()


def draw_main_scene(frame_time):
    stage.draw()
    lands.draw()
    cat.draw()
    man.draw()
    heart.draw()

def draw(frame_time):
    clear_canvas()
    draw_main_scene(frame_time)
    update_canvas()





