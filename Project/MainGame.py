import game_framework
from pico2d import *

import start_state
import title_state
import main_state
import main_state_2
#import gameover_state

open_canvas(1479,600)
game_framework.run(start_state)
close_canvas()