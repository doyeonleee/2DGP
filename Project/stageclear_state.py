import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"



import game_framework
from pico2d import *

import main_state
import main_state_2
import title_state

name = "stageclear"
image = None
bg = None
logo_time = 0.0
counter = 0

def enter():
    global image, bg
    image = load_image('Resources\GameClear\StageClear.png')
    bg = load_image('Resources\GameClear\BG.png')


def exit():
    global image, bg
    del(image)
    del(bg)

def update(frame_time):
    pass

def draw(frame_time):
    global image, counter
    clear_canvas()
    #main_state.draw_main_scene(frame_time)
    bg.draw(740,300)
    image.draw(730,300)
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #if keydown 'p' return to previous state
            print('input')
            game_framework.push_state(main_state_2)
            #game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.push_state(title_state)


def pause(): pass


def resume(): pass