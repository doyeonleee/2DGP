import game_framework
from pico2d import *
from global_values import *

import main_state
import title_state


name = "StartState"
image = None
logo_time = 0.0


window_width = 1479
window_height = 600

def enter():
    global image
    open_canvas(window_width, window_height)
    game_framework.reset_time()
    image = load_image('start_bg.png')


def exit():
    global image
    del(image)
    close_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if( event.type, event.key ) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()



def draw(frame_time):
    clear_canvas()
    image.draw(window_width / 2, window_height / 2)
    update_canvas()

def update(frame_time):
    global logo_time
    if (logo_time > 1.0):
        logo_time = 0
        # game_framework.quit()
        # title image size 1000 x 600 -> change_state
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01


def pause():
    pass


def resume():
    pass





