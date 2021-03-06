import platform
import os

if platform.architecture()[0] == '32bit':
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x86"
else:
    os.environ["PYSDL2_DLL_PATH"] = "./SDL2/x64"



import game_framework
from pico2d import *

import main_state
import main_state_1

name = "TitleState"
image = None
text = None
bgm = None
logo_time = 0.0
counter = 0


window_width = 1479
window_height = 600

def enter():
    global image,text, bgm
    game_framework.reset_time()
    image = load_image('Resources\Title\Title.png')
    text = load_image('Resources\Title\Title_txt.png')
    bgm = load_music('Title.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image,text
    del(image)
    del(text)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if( event.type, event.key ) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif( event.type, event.key ) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(main_state_1)

def draw(frame_time):
    global counter
    clear_canvas()
    image.draw(window_width / 2, window_height / 2)
    if counter < 50:
        text.draw(window_width / 2,150)
    update_canvas()


def update(frame_time):
    global  counter
    counter = (counter + 1) % 100


def pause():
    pass


def resume():
    pass





