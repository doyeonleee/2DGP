import game_framework
from pico2d import *

# fill state here
import start_state
#import title_state
import main_state

open_canvas(1000,600)
game_framework.run(main_state)
close_canvas()