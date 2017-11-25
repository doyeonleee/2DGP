from pico2d import *
from Game_Character import *
from Game_Stage import *

class Camera:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 30cm
    RUN_SPEED_KMPH = 40.0  # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 8
    FRAMES_PER_IDLE_ACTION = 10


    def __init__(self):
        self.x = Cat.x
        self.y = Cat.y

    def handle_event(self,event):
        pass

    def update(self):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))
        print(self.x)
        self.x = clamp(0, self.x, 1800)
