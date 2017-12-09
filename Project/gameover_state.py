import game_framework
from pico2d import *

import main_state
import title_state

name = "gameover"
image = None
bg = None
txt = None
logo_time = 0.0
counter = 0

def enter():
    global image, bg,txt
    image = load_image('Resources\GameOver\GameOver.png')
    bg = load_image('Resources\GameOver\Background.png')
    txt = load_image('Resources\GameOver\GameOver_txt.png')



def exit():
    global image, bg, txt
    del(image)
    del(bg)
    del(txt)


def update(frame_time):
    #counter = image delay
    global counter
    counter = (counter + 1) % 100
    pass

def draw(frame_time):
    global image, counter
    clear_canvas()
    bg.draw(900,300)
    if counter < 50:
        txt.draw(770, 200)
    image.draw(820,500)


    update_canvas()

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            #if keydown 'p' return to previous state
            game_framework.change_state(title_state)



def pause(): pass


def resume(): pass