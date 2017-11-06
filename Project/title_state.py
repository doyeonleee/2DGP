import game_framework
from pico2d import *

import main_state

name = "TitleState"
image = None

#load image( 1000 X 600 )
def enter():
    global image
    #open_canvas(1000, 600)
    image = load_image('title_BackGround.png')


def exit():
    global image
    del(image)


def handle_events():
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



def draw():
    clear_canvas()
    image.draw(500,300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






