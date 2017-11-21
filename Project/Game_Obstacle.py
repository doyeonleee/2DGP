import random

from pico2d import *

#Create Obstacle

class Stone:
    def __init__(self):
        self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\stone.png')

    def draw(self):
        self.image.draw(500,50)

    def get_bb(self):
        pass

    def draw_bb(self):
        pass

class Pumpkin:
    # Pumkin size : 113 X 150 (113cm X 150cm)
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 30cm
    RUN_SPEED_KMPH = 20.0  # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 10

    image = None
    LEFT_WALK, RIGHT_WALK = 0, 1

    def __init__(self):
        self.x, self.y = 1000, 110
        self.walk_frame = random.randint(0, 9)
        self.life_time = 0.0
        self.total_walk_frames = 0.0
        self.frame = 0
        self.dir = 0
        self.state = self.RIGHT_WALK

    # frame == 10
    def update(self, frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))

        self.life_time += frame_time
        distance = Pumpkin.RUN_SPEED_PPS * frame_time
        if self.state in (self.RIGHT_WALK, ):
            #self.total_walk_frames += Pumpkin.FRAMES_PER_RUN_ACTION * Pumpkin.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)
        elif self.state in (self.LEFT_WALK, ):
            #self.total_walk_frames += Pumpkin.FRAMES_PER_RUN_ACTION * Pumpkin.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)

        self.x = clamp(1000, self.x, 1400)
        if(self.x == 1400):
            self.state = self.LEFT_WALK
        elif(self.x == 1000):
            self.state = self.RIGHT_WALK

    def draw(self):
        if self.state == self.RIGHT_WALK:
            if Pumpkin.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Pumpkin_Right.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 132, self.x, self.y)
                self.dir = 1
        elif self.state == self.LEFT_WALK:
            if Pumpkin.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Pumpkin_Left.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 132, self.x, self.y)
                self.dir = -1

    def handle_event(self, event):
        pass

    def get_bb(self):
        pass

    def draw_bb(self):
        pass

class Santa:
    pass

class Zombie:
    # Zombie size : 124 X 150 (124cm X 150cm)
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 30cm
    RUN_SPEED_KMPH = 5.0  # 30km/h
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_RUN_ACTION = 10

    image = None
    LEFT_WALK, RIGHT_WALK = 0, 1

    def __init__(self):
        self.x, self.y = 500, 110
        self.walk_frame = random.randint(0, 9)
        self.life_time = 0.0
        self.total_walk_frames = 0.0
        self.frame = 0
        self.dir = 0
        self.state = self.RIGHT_WALK

    # frame == 10
    def update(self, frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))

        self.life_time += frame_time
        distance = Zombie.RUN_SPEED_PPS * frame_time
        if self.state in (self.RIGHT_WALK,):
            #self.total_walk_frames += Zombie.FRAMES_PER_RUN_ACTION * Zombie.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)
        elif self.state in (self.LEFT_WALK,):
            #self.total_walk_frames += Zombie.FRAMES_PER_RUN_ACTION * Zombie.ACTION_PER_TIME * frame_time
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)

        self.x = clamp(500, self.x, 700)
        if (self.x == 700):
            self.state = self.LEFT_WALK
        elif (self.x == 500):
            self.state = self.RIGHT_WALK

    def draw(self):
        if self.state == self.RIGHT_WALK:
            if Zombie.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Zombie_Right.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 121, self.x, self.y)
                self.dir = 1
        elif self.state == self.LEFT_WALK:
            if Zombie.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Zombie_Left.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 121, self.x, self.y)
                self.dir = -1

    def handle_event(self, event):
        pass

    def get_bb(self):
        pass

    def draw_bb(self):
        pass