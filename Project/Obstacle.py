import random

from pico2d import *
from global_values import window_width, window_height

class Enemy:
    pass
    #Stage1 Enemy

    #Stage2 Enemy

class Zombie:
    # Zombie size : 124 X 150 (124cm X 150cm)
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 30cm
    RUN_SPEED_KMPH = 10.0  # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 10

    image = None
    LEFT_WALK, RIGHT_WALK = 0, 1

    def __init__(self,x, y):
        self.x, self.y = x, y
        self.walk_frame = random.randint(0, 9)
        self.frame = 0
        self.dir = 0
        self.state = self.LEFT_WALK
        zombies.append(self)

    # frame == 10
    def update(self, frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))

        distance = Zombie.RUN_SPEED_PPS * frame_time
        if self.state in (self.RIGHT_WALK,):
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)
        elif self.state in (self.LEFT_WALK,):
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)


    def draw(self):
        if self.state == self.RIGHT_WALK:
            if Zombie.image == None:
                self.image = load_image('Resources\Obstacle\Zombie\Zombie_Right.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 121, self.x, self.y)
                self.dir = 1
        elif self.state == self.LEFT_WALK:
            if Zombie.image == None:
                self.image = load_image('Resources\Obstacle\Zombie\Zombie_Left.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 121, self.x, self.y)
                self.dir = -1

    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Stone:
    def __init__(self, x, y):
        self.image = load_image('Resources\Obstacle\Stone\Stage1_Stone.png')
        self.x = x
        self.y = y
        stones.append(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())