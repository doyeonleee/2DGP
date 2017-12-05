import random

from pico2d import *
from global_values import window_width, window_height

#stage width 5431 x 755px = 5.431km
class Stage:
    image = None
    STAGE1, STAGE2, STAGE3 = 0, 1, 2

    def __init__(self):
        self.image = load_image('Resources\Stage\Stage1\Background\Stage1_BackGround (2).png')
        #self.image= None
        self.canvas_width = window_width
        self.canvas_height = window_height
        self.w = self.image.w
        self.h = self.image.h
        self.bgm = None
        self.state = self.STAGE1

    def set_center_object(self,cat):
        self.center_object = cat

    def stage_clear(self):
        self.state += 1

    def draw(self):
        if self.state == self.STAGE1:
            #self.image = load_image('Resources\Stage\Stage1\Background\BackGround.png')
            self.image.clip_draw_to_origin(
                self.window_left, self.window_bottom,
                self.canvas_width, self.canvas_height,
                0, 0
            )
        elif self.state == self.STAGE2:
            pass
        elif self.state == self.STAGE3:
            pass

    def update(self, frame_time):
        self.window_left = clamp(0,
                                 int(self.center_object.x) - self.canvas_width // 2,
                                 self.w - self.canvas_width)
        self.window_bottom = clamp(0,
                                   int(self.center_object.y) - self.canvas_height // 2,
                                   self.h - self.canvas_height)

    def handle_event(self,event):
        pass


    def __del__(self):
        del self.image
        del self.bgm


class Land:
    def __init__(self,stage):
        self.canvas_width = window_width
        self.canvas_height = window_height
        self.stage = stage
        if self.stage.state == self.stage.STAGE1:
            self.start_land = load_image('Resources\Stage\Stage1\Land\Land_Start.png')
            self.start_x, self.start_y = 750 , 50

            self.road1 = load_image('Resources\Stage\Stage1\Land\Land_Basic.png')
            self.road1_x, self.road1_y = 40 , 4
            self.road2 = load_image('Resources\Stage\Stage1\Land\Land_Basic.png')
            self.road2_x, self.road2_y = 1500, 4
            self.road3 = load_image('Resources\Stage\Stage1\Land\Land_Basic.png')
            self.road3_x, self.road3_y = 3500, 4
            self.road4 = load_image('Resources\Stage\Stage1\Land\Land_Basic.png')
            self.road4_x, self.road4_y = 3900, 4
            self.road5 = load_image('Resources\Stage\Stage1\Land\Land_Basic.png')
            self.road5_x, self.road5_y = 4100, 4
            self.road6 = load_image('Resources\Stage\Stage1\Land\Land_Basic.png')
            self.road6_x, self.road6_y = 4500, 4

            self.skyroad1 = load_image('Resources\Stage\Stage1\Land\Land_Basic_2.png')
            self.skyroad1_x, self.skyroad1_y = 2100, 150

            self.zombie_land = load_image('Resources\Stage\Stage1\Land\Land_Zombie.png')
            self.zombie_x,self.zombie_y = 2800, 70

        elif self.stage.state == self.stage.STAGE2:
            pass
        elif self.stage.state == self.stage.STAGE3:
            pass

    def draw(self):
        if self.stage.state == self.stage.STAGE1:
            self.start_land.draw(self.start_x - self.stage.window_left, self.start_y - self.stage.window_bottom)

            self.road1.draw(self.road1_x - self.stage.window_left, self.road1_y - self.stage.window_bottom)
            self.road2.draw(self.road2_x - self.stage.window_left, self.road2_y - self.stage.window_bottom)
            self.road3.draw(self.road3_x - self.stage.window_left, self.road3_y - self.stage.window_bottom)
            self.road4.draw(self.road4_x - self.stage.window_left, self.road4_y - self.stage.window_bottom)
            self.road5.draw(self.road5_x - self.stage.window_left, self.road5_y - self.stage.window_bottom)
            self.road6.draw(self.road6_x - self.stage.window_left, self.road6_y - self.stage.window_bottom)

            self.skyroad1.draw(self.skyroad1_x - self.stage.window_left, self.skyroad1_y - self.stage.window_bottom)

            self.zombie_land.draw(self.zombie_x - self.stage.window_left, self.zombie_y - self.stage.window_bottom)

        elif self.stage.state == self.stage.STAGE2:
            pass

        elif self.stage.state == self.stage.STAGE3:
            pass

    def update(self,frame_time):
        pass

    def draw_bb(self):
        pass

    def get_bb(self):
        pass



