import random

from pico2d import *
from collision import *
from global_values import window_width, window_height

#stage width 5431 x 755px = 5.431km
class Stage:
    image = None
    bgm = None
    STAGE1, STAGE2 = 0, 1

    def __init__(self):
        self.canvas_width = window_width
        self.canvas_height = window_height
        self.state = self.STAGE2
        self.image = load_image('Resources\Stage\Stage2\Background\Stage2_BackGround.png')
        self.w = self.image.w
        self.h = self.image.h
        if self.bgm == None:
            self.bgm = load_music('Stage2.ogg')
            self.bgm.set_volume(64)
            self.bgm.repeat_play()


    def set_center_object(self,cat):
        self.center_object = cat

    def draw(self):
            self.image.clip_draw_to_origin(
                self.window_left, self.window_bottom,
                self.canvas_width, self.canvas_height,
                0, 0
            )


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
        #self.roads = []
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

        self.skyroad = load_image('Resources\Stage\Stage1\Land\Land_Basic_2.png')
        self.skyroad_x, self.skyroad_y = 2100, 150

        self.zombie_land = load_image('Resources\Stage\Stage1\Land\Land_Zombie.png')
        self.zombie_x,self.zombie_y = 2800, 70


    def draw(self):
            self.start_land.draw(self.start_x - self.stage.window_left, self.start_y - self.stage.window_bottom)

            self.water_1.draw(self.water_1_x - self.stage.window_left, self.water_1_y - self.stage.window_bottom)
            self.water_2.draw(self.water_2_x - self.stage.window_left, self.water_2_y - self.stage.window_bottom)
            self.water_3.draw(self.water_3_x - self.stage.window_left, self.water_3_y - self.stage.window_bottom)
            self.water_4.draw(self.water_4_x - self.stage.window_left, self.water_4_y - self.stage.window_bottom)
            self.water_5.draw(self.water_5_x - self.stage.window_left, self.water_5_y - self.stage.window_bottom)

            self.road2.draw(self.road2_x - self.stage.window_left, self.road2_y - self.stage.window_bottom)
            self.road3.draw(self.road3_x - self.stage.window_left, self.road3_y - self.stage.window_bottom)
            self.road4.draw(self.road4_x - self.stage.window_left, self.road4_y - self.stage.window_bottom)
            self.road5.draw(self.road5_x - self.stage.window_left, self.road5_y - self.stage.window_bottom)
            self.road6.draw(self.road6_x - self.stage.window_left, self.road6_y - self.stage.window_bottom)

            self.skyroad.draw(self.skyroad_x - self.stage.window_left, self.skyroad_y - self.stage.window_bottom)
            #self.skyroad.draw(self.skyroad_x + 1400 - self.stage.window_left, self.skyroad_y - self.stage.window_bottom)


    def update(self,frame_time):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
        #draw_rectangle(self.start_x - 300 - self.stage.window_left, self.start_y - 10 - self.stage.window_bottom,
        #               self.start_x + 350 - self.stage.window_left, self.start_y + 15 - self.stage.window_bottom)
        #draw_rectangle(self.road2_x - 300 - self.stage.window_left, self.road2_y - 30 - self.stage.window_bottom,
        #               self.road2_x + 300 - self.stage.window_left, self.road2_y + 60 - self.stage.window_bottom)
        #draw_rectangle(self.road3_x - 300 - self.stage.window_left, self.road3_y - 30 - self.stage.window_bottom,
        #               self.road3_x + 300 - self.stage.window_left, self.road3_y + 60 - self.stage.window_bottom)
        #draw_rectangle(self.road4_x - 300 - self.stage.window_left, self.road4_y - 30 - self.stage.window_bottom,
        #               self.road4_x + 300 - self.stage.window_left, self.road4_y + 60 - self.stage.window_bottom)
        #draw_rectangle(self.road5_x - 300 - self.stage.window_left, self.road5_y - 30 - self.stage.window_bottom,
        #               self.road5_x + 300 - self.stage.window_left, self.road5_y + 60 - self.stage.window_bottom)
        #draw_rectangle(self.road6_x - 300 - self.stage.window_left, self.road6_y - 30 - self.stage.window_bottom,
        #               self.road6_x + 300 - self.stage.window_left, self.road6_y + 60 - self.stage.window_bottom)
        #draw_rectangle(self.skyroad1_x - 230 - self.stage.window_left, self.skyroad1_y - 35 - self.stage.window_bottom,
        #               self.skyroad1_x + 230 -  self.stage.window_left, self.skyroad1_y + 35 - self.stage.window_bottom)
        #draw_rectangle(self.zombie_x - 400 - self.stage.window_left, self.zombie_y - 50 - self.stage.window_bottom,
        #               self.zombie_x + 270 - self.stage.window_left, self.zombie_y - self.stage.window_bottom)

    def get_bb(self):
        if self.skyroad:
            return self.skyroad_x - 200 - self.stage.window_left, self.skyroad_y - 35 - self.stage.window_bottom, \
                       self.skyroad_x + 200 -  self.stage.window_left, self.skyroad_y + 35 - self.stage.window_bottom

        #if self.zombie_land:
        #    return self.zombie_x - 400 - self.stage.window_left, self.zombie_y - 50 - self.stage.window_bottom, \
        #               self.zombie_x + 270 - self.stage.window_left, self.zombie_y - self.stage.window_bottom
        #if self.start_land:
        #    return self.start_x - 300 - self.stage.window_left, self.start_y - 10 - self.stage.window_bottom,   \
        #               self.start_x + 350 - self.stage.window_left, self.start_y + 15 - self.stage.window_bottom
        #if self.road2:
        #    return self.road2_x - 300 - self.stage.window_left, self.road2_y - 30 - self.stage.window_bottom,   \
        #               self.road2_x + 300 - self.stage.window_left, self.road2_y + 60 - self.stage.window_bottom
        #if self.road3:
        #    return self.road3_x - 300 - self.stage.window_left, self.road3_y - 30 - self.stage.window_bottom,   \
        #               self.road3_x + 300 - self.stage.window_left, self.road3_y + 60 - self.stage.window_bottom
        #if self.road4:
        #    return self.road4_x - 300 - self.stage.window_left, self.road4_y - 30 - self.stage.window_bottom,   \
        #               self.road4_x + 300 - self.stage.window_left, self.road4_y + 60 - self.stage.window_bottom
        #if self.road5:
        #    return self.road5_x - 300 - self.stage.window_left, self.road5_y - 30 - self.stage.window_bottom,   \
        #               self.road5_x + 300 - self.stage.window_left, self.road5_y + 60 - self.stage.window_bottom
        #if self.road6:
        #    return self.road6_x - 300 - self.stage.window_left, self.road6_y - 30 - self.stage.window_bottom,   \
        #               self.road6_x + 300 - self.stage.window_left, self.road6_y + 60 - self.stage.window_bottom


    def stop(self,obj):
            obj.y = 240
            obj.jump_speed = 0

