import game_framework
from pico2d import *

import main_state

name = "TitleState"
image = None
text = None
logo_time = 0.0
counter = 0

#load image( 1800 X 900 )
def enter():
    global image,text
    game_framework.reset_time()
    image = load_image('title.png')
    text = load_image('title_txt.png')

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
                game_framework.change_state(main_state)
                #game_framework.quit()



def draw(frame_time):
    global counter
    clear_canvas()
    image.draw(900,450)
    if counter < 50:
        text.draw(900,150)
    update_canvas()


def update(frame_time):
    global  counter
    counter = (counter + 1) % 100


def pause():
    pass


def resume():
    pass





