import game_framework
from pico2d import *

import main_state_2
import title_state

name = "gameover"
image = None
bg = None
logo_time = 0.0
counter = 0

def enter():
    global image, bg
    image = load_image('Resources\GameClear\StageClear.png')
    bg = load_image('Resources\GameClear\BackGround.png')


def exit():
    global image, bg
    del(image)
    del(bg)

def update(frame_time):
    pass

def draw(frame_time):
    global image, counter
    clear_canvas()
    #main_state_2.draw_main_scene(frame_time)
    bg.draw(900,300)
    image.draw(730,300)
    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            #if keydown 'p' return to previous state
            game_framework.push_state(main_state_2)
            #game_framework.quit()


def pause(): pass


def resume(): pass