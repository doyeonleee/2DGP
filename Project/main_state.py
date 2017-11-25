import random
import json
import os
from global_values import *
import global_values

from pico2d import *
from Game_Stage import Stage1, BackGround
from Game_Character import Cat, Man
from Game_Heart import Heart
from Game_Obstacle import Stone, Pumpkin, Zombie

import game_framework
import title_state
import gameover_state

name = "MainState"
cat = None
stage = None
heart = None
pumpkin = None
zombie = None
font = None
CHARACTER_RUNNING = False
background_image = None

def create_objects():
    global cat, stage, heart, stone, man, pumpkin, zombie, background_image
    cat = Cat()
    stage = Stage1()
    heart = Heart()
    stone = Stone()
    pumpkin = Pumpkin()
    zombie = Zombie()
    man = Man()
    background_image = BackGround()



def enter():
    #open_canvas(1479,600)
    game_framework.reset_time()
    create_objects()


def exit():
    global cat, stage, heart, stone, man, pumpkin, zombie, background_image
    del(cat)
    del(stage)
    del(heart)
    del(stone)
    del(man)
    del(pumpkin)
    del(zombie)
    del(background_image)
    #close_canvas()

def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global CHARACTER_RUNNING

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        else:
            CHARACTER_RUNNING = True
            cat.handle_event(event)
            stage.handle_event(event)
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
        #    game_framework.push_state(pause_state)


def collide(a,b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def update(frame_time):
    cat.update(frame_time)
    stage.update(frame_time)
    pumpkin.update(frame_time)
    zombie.update(frame_time)

    if collide(cat,pumpkin):
        #heart.attacked()
        pass

    if collide(cat,zombie):
        #heart.attacked()
        pass

    if collide(cat,stone):
        #heart.attacked()
        pass

    if( heart.state == heart.DIE):
        game_framework.change_state(gameover_state)

    update_canvas()


def draw_main_scene(frame_time):
    #stage.draw(frame_time)
    background_image.draw()
    cat.draw()
    stone.draw()
    man.draw()
    pumpkin.draw()
    zombie.draw()
    heart.draw()

    #zombie.draw_bb()
    #pumpkin.draw_bb()
    #man.draw_bb()
    #stone.draw_bb()
    #cat.draw_bb()


def draw(frame_time):
    clear_canvas()
    draw_main_scene(frame_time)


    update_canvas()





