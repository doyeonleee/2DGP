import random

from pico2d import *

#Create Cat
class Cat:
    # Cat size : 100 X 100 (100cm X 100cm)
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 30cm
    RUN_SPEED_KMPH = 30.0  # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 8
    FRAMES_PER_IDLE_ACTION = 10

    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_IDLE, RIGHT_IDLE = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.idle_frame = random.randint(0, 7)
        self.run_frame = random.randint(0, 9)
        self.life_time = 0.0
        self.total_idle_frames = 0.0
        self.total_run_frames = 0.0
        self.frame = 0
        self.dir = 0
        self.state = self.RIGHT_IDLE

    #RUN = 8, IDLE = 10
    # frame == RUN = 8, IDLE = 10
    def update(self, frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))

        self.life_time += frame_time
        distance = Cat.RUN_SPEED_PPS * frame_time
        if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
            self.total_idle_frames += Cat.FRAMES_PER_IDLE_ACTION * Cat.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)
        elif self.state in (self.RIGHT_RUN, self.LEFT_RUN):
            self.total_run_frames += Cat.FRAMES_PER_RUN_ACTION * Cat.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * distance)

        self.x = clamp(0, self.x, 1000)

    def draw(self):
        if self.state == self.RIGHT_IDLE:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_Right_Idle2.png')
                self.image.clip_draw(self.frame * 98, 0, 89, 90, self.x, self.y)
                self.dir = 0
        elif self.state == self.LEFT_IDLE:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_LEFT_Idle2.png')
                self.image.clip_draw(self.frame * 98, 0, 89, 90, self.x, self.y)
                self.dir = 0
        elif self.state == self.RIGHT_RUN:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_Right_RUN.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 101, self.x, self.y)
                self.dir = 1
        elif self.state == self.LEFT_RUN:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_LEFT_RUN.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 101, self.x, self.y)
                self.dir = -1

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
                self.state = self.LEFT_RUN
            if self.state == self.RIGHT_RUN:
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
                self.state = self.RIGHT_RUN
            if self.state == self.LEFT_RUN:
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_IDLE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_IDLE

#Create Man
class Man:
    def __init__(self):
        self.x, self.y = 900, 120
        self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Man2.png')

    def draw(self):
        self.image.draw(self.x, self.y)
