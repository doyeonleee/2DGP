import random

from pico2d import *
from global_values import window_width, window_height

class Enemy:
    # Stage1 Zombie
    # Zombie size : 100 X 121 (100cm X 121cm)
    PIXEL_PER_METER = (10.0 / 0.3)  # 10pixel = 10cm
    ZOMBIE_WALK_SPEED_KMPH = 50.0   # 10km/h
    ZOMBIE_WALK_SPEED_MPM = (ZOMBIE_WALK_SPEED_KMPH * 1000.0 / 60.0)
    ZOMBIE_WALK_SPEED_MPS = (ZOMBIE_WALK_SPEED_MPM / 60.0)
    ZOMBIE_WALK_SPEED_PPS = (ZOMBIE_WALK_SPEED_MPS * PIXEL_PER_METER)
    ZOMBIE_FRAMES_PER_WALK_ACTION = 10

    PUMKIN_WALK_SPEED_KMPH = 50.0
    PUMKIN_WALK_SPEED_KMPH = 50.0  # 10km/h
    PUMKIN_WALK_SPEED_MPM = (PUMKIN_WALK_SPEED_KMPH * 1000.0 / 60.0)
    PUMKIN_WALK_SPEED_MPS = (PUMKIN_WALK_SPEED_MPM / 60.0)
    PUMKIN_WALK_SPEED_PPS = (PUMKIN_WALK_SPEED_MPS * PIXEL_PER_METER)
    PUMKIN_FRAMES_PER_WALK_ACTION = 10

    SANTA_WALK_SPEED_KMPH = 50.0
    SANTA_WALK_SPEED_KMPH = 50.0  # 10km/h
    SANTA_WALK_SPEED_MPM = (SANTA_WALK_SPEED_KMPH * 1000.0 / 60.0)
    SANTA_WALK_SPEED_MPS = (SANTA_WALK_SPEED_MPM / 60.0)
    SANTA_WALK_SPEED_PPS = (SANTA_WALK_SPEED_MPS * PIXEL_PER_METER)
    SANTA_FRAMES_PER_WALK_ACTION = 13

    image = None
    ZOMBIE, PUMKIN, SANTA = 0, 1, 2
    LEFT_WALK, RIGHT_WALK = 0, 1

    def __init__(self,stage):
        #self.canvas_width = window_width
        #self.canvas_height = window_height
        self.stage = stage
        if self.stage.state == self.stage.STAGE1:
            self.enemy_status = self.ZOMBIE
            self.walk_frame = random.randint(0,9)
            self.dir = 0
            self.state = self.LEFT_WALK
            self.x, self.y = 2500, 120
            self.x1, self.y1 = 3800, 120
        elif self.stage.state == self.stage.STAGE2:
            self.enemy_status = self.SANTA
            self.walk_frame = random.randint(0,12)
            self.dir = 0
            self.state = self.LEFT_WALK
            self.x, self.y = 1299, 120
            self.x1, self.y1 = 3800, 120

    def update(self,frame_time):
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))
        distance = Enemy.ZOMBIE_WALK_SPEED_PPS * frame_time
        if self.enemy_status == self.ZOMBIE:
            clamp(2500,self.x, 3000)
            clamp(3500, self.x1, 4000)
            if self.x <= 2500:
                self.state = self.RIGHT_WALK
            elif self.x >= 3000:
                self.state = self.LEFT_WALK

            if self.x1 <= 3500:
                self.state = self.RIGHT_WALK
            elif self.x1 >= 4000:
                self.state = self.LEFT_WALK

            if self.state in (self.RIGHT_WALK,):
                self.dir = 1
                self.walk_frame = (self.walk_frame + 1) % self.ZOMBIE_FRAMES_PER_WALK_ACTION
                self.x += (self.dir * distance)
                self.x1 += (self.dir * distance)

            elif self.state in (self.LEFT_WALK,):
                self.dir = -1
                self.walk_frame = (self.walk_frame + 1) % self.ZOMBIE_FRAMES_PER_WALK_ACTION
                self.x += (self.dir * distance)
                self.x1 += (self.dir * distance)

        elif self.enemy_status == self.SANTA:
            #clamp(2500, self.x, 3000)
            #clamp(3500, self.x1, 4000)
            if self.x <= 1000:
                self.state = self.RIGHT_WALK
            elif self.x >= 1500:
                self.state = self.LEFT_WALK

            if self.x1 <= 3500:
                self.state = self.RIGHT_WALK
            elif self.x1 >= 4000:
                self.state = self.LEFT_WALK

            if self.state in (self.RIGHT_WALK,):
                self.dir = 1
                self.walk_frame = (self.walk_frame + 1) % self.SANTA_FRAMES_PER_WALK_ACTION
                self.x += (self.dir * distance)
                self.x1 += (self.dir * distance)

            elif self.state in (self.LEFT_WALK,):
                self.dir = -1
                self.walk_frame = (self.walk_frame + 1) % self.SANTA_FRAMES_PER_WALK_ACTION
                self.x += (self.dir * distance)
                self.x1 += (self.dir * distance)


    def draw(self):
        #zombie walk frame width 100, height 121
        if self.enemy_status == self.ZOMBIE:
            if self.state == self.RIGHT_WALK:
                self.image = load_image('Resources\Obstacle\Stage1\Zombie\Zombie_Right.png')
                self.image.clip_draw(self.walk_frame * 100, 0, 100, 121,
                                     self.x - self.stage.window_left, self.y - self.stage.window_bottom)

                self.image.clip_draw(self.walk_frame * 100, 0, 100, 121,
                                     self.x1 - self.stage.window_left, self.y1 - self.stage.window_bottom)

                self.dir = 1
            elif self.state == self.LEFT_WALK:
                self.image = load_image('Resources\Obstacle\Stage1\Zombie\Zombie_Left.png')
                self.image.clip_draw(self.walk_frame * 100, 0, 100, 121,
                                     self.x - self.stage.window_left, self.y - self.stage.window_bottom)

                self.image.clip_draw(self.walk_frame * 100, 0, 100, 121,
                                     self.x1 - self.stage.window_left, self.y1 - self.stage.window_bottom)

                self.dir = -1

        elif self.enemy_status == self.SANTA:
            if self.state == self.RIGHT_WALK:
                self.image = load_image('Resources\Obstacle\Stage2\Santa\Santa_Right.png')
                self.image.clip_draw(self.walk_frame * 77, 0, 77, 121,
                                     self.x - self.stage.window_left, self.y - self.stage.window_bottom)

                self.image.clip_draw(self.walk_frame * 77, 0, 77, 121,
                                     self.x1 - self.stage.window_left, self.y1 - self.stage.window_bottom)

                self.dir = 1
            elif self.state == self.LEFT_WALK:
                self.image = load_image('Resources\Obstacle\Stage2\Santa\Santa_Left.png')
                self.image.clip_draw(self.walk_frame * 77, 0, 77, 121,
                                     self.x - self.stage.window_left, self.y - self.stage.window_bottom)

                self.image.clip_draw(self.walk_frame * 77, 0, 77, 121,
                                     self.x1 - self.stage.window_left, self.y1 - self.stage.window_bottom)

                self.dir = -1


    def handle_event(self, event):
        pass

    def get_bb(self):
        return self.x - 20 - self.stage.window_left, self.y - 20 - self.stage.window_bottom, \
               self.x + 20 - self.stage.window_left, self.y + 20- self.stage.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


class Stone:
    def __init__(self, stage):
        self.stage = stage
        if self.stage.state == self.stage.STAGE1:
            self.image = load_image('Resources\Obstacle\Stage1\Stage1_Stone.png')
            self.x, self.y = 1500, 80
            #self.x1, self.y1 = 1500, 80
            self.x2, self.y2 = 3000, 80
            self.x3, self.y3 = 3500, 80
            self.x4, self.y4 = 4000, 80

        elif self.stage.state == self.stage.STAGE2:
            self.image = load_image('Resources\Obstacle\Stage2\Stage2_Stone.png')
            self.x, self.y = 1300, 80
            # self.x1, self.y1 = 1500, 80
            self.x2, self.y2 = 3000, 80
            self.x3, self.y3 = 3500, 80
            self.x4, self.y4 = 4000, 80

    def draw(self):
        self.image.draw(self.x - self.stage.window_left, self.y - self.stage.window_bottom)
        #self.image.draw(self.x1 - self.stage.window_left, self.y1 - self.stage.window_bottom)
        self.image.draw(self.x2 - self.stage.window_left, self.y2 - self.stage.window_bottom)
        self.image.draw(self.x3 - self.stage.window_left, self.y3 - self.stage.window_bottom)
        self.image.draw(self.x4 - self.stage.window_left, self.y4 - self.stage.window_bottom)

    def get_bb(self):
        return self.x - 30 - self.stage.window_left, self.y - 20 - self.stage.window_bottom, \
               self.x + 30 - self.stage.window_left, self.y + 20 - self.stage.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())