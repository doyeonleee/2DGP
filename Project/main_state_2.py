import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"



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

from Stage2 import Stage as Background
from Stage import Land as Land
from Life import Heart as Heart
from Character import Cat as Cat
from Character import Man as Man
from Obstacle import Enemy as Enemy
from Obstacle import Stone as Stone

from global_values import window_height, window_width

name = "main_state"

stage = None
cat = None
man = None
lands = None
heart = None
enemy = None
stone = None

def create_objects():
    global stage, cat, lands, man, heart, enemy, stone
    stage = Background()
    cat = Cat()
    heart = Heart()
    lands = Land(stage)
    man = Man(stage)
    enemy = Enemy(stage)
    stone = Stone(stage)
    stage.set_center_object(cat)
    cat.set_background(stage)

def delete_objects():
    global stage, cat, lands, man, heart, enemy, stone
    del(stage)
    del(cat)
    del(lands)
    del(man)
    del(heart)
    del(enemy)
    del(stone)

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
    enemy.update(frame_time)

    if collide(cat,stone):
        heart.attacked()

    if collide(cat,enemy):
        heart.attacked()

    if collide(cat,lands):
        lands.stop(cat)

    if heart.state == heart.DIE:
        game_framework.push_state(gameover_state)

    #클리어 조건
    if cat.x >= 5000:
        game_framework.push_state(stageclear_state)

    update_canvas()


def draw_main_scene(frame_time):
    stage.draw()
    stone.draw()
    lands.draw()
    cat.draw()
    enemy.draw()
    man.draw()
    heart.draw()

    #stone.draw_bb()
    #lands.draw_bb()
    #cat.draw_bb()
    #enemy.draw_bb()
    #man.draw_bb()


def draw(frame_time):
    clear_canvas()
    draw_main_scene(frame_time)
    update_canvas()





