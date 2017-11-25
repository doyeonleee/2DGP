from pico2d import *

from global_values import *
from Game_Character import *

import main_state
#Create Stage

global CHARACTER_RUNNING

class Create_Stage:
    pass


class Stage1:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 30cm
    RUN_SPEED_KMPH = 50.0  # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 8
    FRAMES_PER_IDLE_ACTION = 10
    MAP_MOVE = 0
    MOVE_STATUS = False

    def __init__(self):
        self.image = load_image('test.png')
        self.x = window_width / 2
        self.y = window_height / 2
        self.dir = 0


    def draw(self, frame_time):
        self.image.clip_draw(self.MAP_MOVE, 0, window_width, window_height, self.x, self.y)

    def get_bb(self):
        pass

    def draw_bb(self):
        pass

    def update(self,frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))
        #if CHARACTER_RUNNING == True:
        if (self.MOVE_STATUS == True):
            self.MAP_MOVE += self.dir * 20
        #clamp(0,self.MAP_MOVE, stage_1_size - window_width - 500)

        if (self.MAP_MOVE < 0):
            self.MAP_MOVE = 0
        elif (self.MAP_MOVE >= stage_1_size - window_width):
            self.MAP_MOVE = stage_1_size - window_width
        #print(self.MAP_MOVE)

    def handle_event(self,event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.dir = -1
            self.MOVE_STATUS = True
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.dir = 1
            self.MOVE_STATUS = True
        else:
            self.MOVE_STATUS = False
            self.dir = 0

class BackGround:
    # image size = 1479 x 600

    def __init__(self):
        self.image = load_image('background_stage_1.png')
        self.BG_x = 740

    def draw(self):
        self.image.draw(self.BG_x, 300)

