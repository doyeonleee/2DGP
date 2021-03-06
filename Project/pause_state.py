import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"


import game_framework
from pico2d import *

import title_state
import main_state

name = "PauseState"
image = None
logo_time = 0.0
counter = 0

def enter():
    global image
    #open_canvas()
    if image == None:
        image = load_image('background_stage_1.png')


def exit():
    global image
    del(image)
    #close_canvas()


def update():
    #counter = image delay
    global counter
    counter = (counter + 1) % 100
    pass

def draw():

    global image, counter
    clear_canvas()
    main_state_2.draw_main_scene()
    if counter < 50:
        image.draw(400,300)
    update_canvas()




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            #if keydown 'p' return to previous state
            game_framework.pop_state()

    pass


def pause(): pass


def resume(): pass