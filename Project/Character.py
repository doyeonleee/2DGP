import random

from pico2d import *
from global_values import window_width, window_height


class Cat:
    image = None
    # Cat size : 100 X 100 (100cm X 100cm)
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 10cm
    RUN_SPEED_KMPH = 100.0          # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 8
    FRAMES_PER_IDLE_ACTION = 10

    LEFT_RUN, RIGHT_RUN, LEFT_IDLE, RIGHT_IDLE, JUMP = 0, 1, 2, 3, 4

    HANDLE_STATE = {
        #LEFT_RUN : HANDLE_LEFT_RUN
        #RIGHT_RUN : HANDLE_RIGHT_RUN
        #LEFT_STAND : HANDLE_LEFT_STAND
        #RIGHT_STAND : HANDLE_RIGHT_STAND
    }

    def __init__(self):
        self.x, self.y = 300, 0
        self.canvas_width = window_width
        self.canvas_height = window_height
        self.idle_frame = random.randint(0, 7)
        self.run_frame = random.randint(0, 9)
        self.dir = 0
        self.jump_speed = 0
        self.state = self.RIGHT_IDLE

    #starting point
    def set_background(self,bg):
        self.bg = bg
        self.x = self.bg.w / 2 - 2015
        print(self.x,self.y)


    def update(self, frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))

        distance = Cat.RUN_SPEED_PPS * frame_time

        if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
            self.idle_frame = (self.idle_frame + 1) % self.FRAMES_PER_IDLE_ACTION
            self.x += (self.dir * distance)

        elif self.state in (self.RIGHT_RUN, self.LEFT_RUN):
            self.run_frame = (self.run_frame + 1) % self.FRAMES_PER_RUN_ACTION
            self.x += (self.dir * distance)

        #self.state == JUMP
        if (self.jump_speed > 0):
            self.y += (self.jump_speed * distance)
            self.y = clamp(0, self.y, 500)
        else:
            self.y += (self.jump_speed * distance)

        if (self.y >= 500):
            self.jump_speed = -1

        if (self.y <= 110):
            self.jump_speed = 0
            self.y = 110

    def draw(self):
        # idle frame width 98 , cat size = 89 x 90 (px)
        # run frame width 100 , cat size = 100 x 101 (px)
        if self.state == self.RIGHT_IDLE:
            if Cat.image == None:
                self.image = load_image('Resources\Character\Cat\Cat_Right_Idle.png')
                self.image.clip_draw(self.idle_frame * 98, 0, 98, 90, self.canvas_width // 2, self.y)
                self.dir = 0
        elif self.state == self.LEFT_IDLE:
            if Cat.image == None:
                self.image = load_image('Resources\Character\Cat\Cat_LEFT_Idle.png')
                self.image.clip_draw(self.idle_frame * 98, 0, 98, 90, self.canvas_width // 2, self.y)
                self.dir = 0
        elif self.state == self.RIGHT_RUN:
            if Cat.image == None:
                self.image = load_image('Resources\Character\Cat\Cat_Right_RUN.png')
                self.image.clip_draw(self.run_frame * 100, 0, 100, 101, self.canvas_width // 2, self.y)
                self.dir = 1
        elif self.state == self.LEFT_RUN:
            if Cat.image == None:
                self.image = load_image('Resources\Character\Cat\Cat_LEFT_RUN.png')
                self.image.clip_draw(self.run_frame * 100, 0, 100, 101, self.canvas_width // 2, self.y)
                self.dir = -1

    def handle_event(self, event):
        global cat_run_status
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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #self.state = JUMP
            self.jump_speed = 1


    def get_bb(self):
        return self.x - 20, self.y - 35, self.x + 20, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def stop(self, master):
        pass

class Man:
    def __init__(self, stage):
        self.canvas_width = window_width
        self.canvas_height = window_height
        self.stage = stage
        self.x, self.y = 4780, 150
        self.image = load_image('Resources\Character\Man\Man.png')

    def draw(self):
        self.image.draw(self.x - self.stage.window_left, self.y - self.stage.window_bottom)

    def get_bb(self):
        return self.x - 75, self.y - 70, self.x + 75, self. y + 70

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def update(self,frame_time):
        pass