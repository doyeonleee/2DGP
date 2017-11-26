import random
import json
import os

import game_framework
import gameover_state
import title_state
import pause_state
import stageclear_state

from pico2d import *
from collision import *

name = "main_state"

cat = None
background = None
heart = None
stones = []
zombies = []
land = []
man = []

window_width = 1479
window_height = 600

stage_size = 7395

move_frames = 0

cat_run_status = False


# object class
class Heart:
    FIRST, SECOND, THIRD, LAST, DIE = 0, 1, 2, 3, 4
    def __init__(self):
        self.x, self.y = 1400, 500
        self.image = None
        self.state = self.FIRST

    def attacked(self):
        self.state += 1
        if (self.state == self.DIE):
            #game_framework.pop_state()
            pass

    def draw(self):
        if(self.state == self.FIRST):
            self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Heart1.png')
            self.image.draw(self.x, self.y)
        elif (self.state == self.SECOND):
            self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Heart2.png')
            self.image.draw(self.x, self.y)
        elif (self.state == self.THIRD):
            self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Heart3.png')
            self.image.draw(self.x, self.y)
        elif (self.state == self.LAST):
            self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Heart4.png')
            self.image.draw(self.x, self.y)

class Cat:
    image = None
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

    LEFT_RUN, RIGHT_RUN, LEFT_IDLE, RIGHT_IDLE = 0, 1, 2, 3


    def __init__(self):
        self.x, self.y = 300, 110
        self.idle_frame = random.randint(0, 7)
        self.run_frame = random.randint(0, 9)
        self.frame = 0
        self.dir = 0
        self.state = self.RIGHT_IDLE
        self.jump_speed = 0

    def update(self, frame_time):
        global land, zombies, stones
        def clamp(minimun, x, maximum):
            return max(minimun, min(x, maximum))

        distance = Cat.RUN_SPEED_PPS * frame_time
        if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
            self.frame = (self.frame + 1) % 10
            self.x += (self.dir * distance)
        elif self.state in (self.RIGHT_RUN, self.LEFT_RUN):
            if self.state == self.RIGHT_RUN:
                for lands in land:
                    lands.x -= distance
                for zombie in zombies:
                    zombie.x -= distance
                for stone in stones:
                    stone.x -= distance
                for master in man:
                    master.x -= distance

            elif self.state == self.LEFT_RUN:
                for lands in land:
                    lands.x += distance
                for zombie in zombies:
                    zombie.x += distance
                for stone in stones:
                    stone.x += distance
                for master in man:
                    master.x += distance


            self.frame = (self.frame + 1) % 8
            self.x += (self.dir * distance)

        if (self.jump_speed > 0):
            self.y += (self.jump_speed * distance)
            self.y = clamp(0, self.y, 300)
        else:
            self.y += (self.jump_speed * distance)

        if (self.y >= 300):
            self.jump_speed = -3

        if (self.y <= 110):
            self.jump_speed = 0
            self.y = 110
        self.x = clamp(10, self.x, window_width - 10)

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
        global cat_run_status
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            cat_run_status = True
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
                self.state = self.LEFT_RUN
            if self.state == self.RIGHT_RUN:
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            cat_run_status = True
            if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
                self.state = self.RIGHT_RUN
            if self.state == self.LEFT_RUN:
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            cat_run_status = False
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_IDLE
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            cat_run_status = False
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_IDLE
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            self.jump_speed = 3


    def get_bb(self):
        return self.x - 20, self.y - 35, self.x + 20, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def stop(self, master):
        self.x = master.x - 80

class BackGround:
    # image size = 1479 x 600
    def __init__(self):
        self.image = load_image('background_stage_1.png')
        self.x = window_width / 2
        self.y = window_height / 2
        self.move_frame = 0

    def draw(self):
        global move_frames
        #self.image.clip_draw(move_frames, 0, window_width, window_height, self.x, self.y)
        self.image.draw(self.x, self.y)

    def update(self,frame_time):
        global move_frames
        if cat_run_status == True:
            move_frames += cat.dir * 40

        if move_frames < 0:
            move_frames = 0
        elif move_frames > stage_size - window_width:
            move_frames = stage_size - window_width

        #print(move_frames)

class Land:
    def __init__(self, x , y, image_name):
        self.image_tmp = image_name
        if image_name == None:
            self.image = load_image('land_basic.png')
        else:
            self.image = load_image(image_name)
        self.x = x
        self.y = y
        land.append(self)

    def draw(self):
         self.image.draw(self.x, self.y)

    def get_bb(self):
        if self.image_tmp == 'land_start.png':
            return self.x - 400, self.y - 10, self.x + 350, self.y + 20
        elif self.image_tmp == 'land_zombie.png':
            return self.x - 400, self.y - 20, self.x + 280, self.y - 5
        else:
            return self.x - 320, self.y +30, self.x + 320, self.y + 60

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Man:
    def __init__(self,x , y):
        self.x, self.y = x, y
        self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Man.png')
        man.append(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 75, self.y - 70, self.x + 75, self. y + 70

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

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
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

class Stone:
    def __init__(self, x, y):
        self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\stone.png')
        self.x = x
        self.y = y
        stones.append(self)

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x + 30, self.y + 20

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

# create_function
def create_lands():
    start_land = Land(390, 50, 'land_start.png')

    #for i in range(2):
    #    lands = Land(random.randint(390,1600), 0, None)

    road_1 = Land(1300, 5, None)

    zombie_land = Land(2200, 70, 'land_zombie.png')

    for i in range(10):
        roads = Land(random.randint(2300,4000), 5, None)

def create_zombies():
    global move_frames
    for i in range(1):
        #zombie = Zombie(random.randint(move_frames,move_frames + window_width), 90)
        zombie = Zombie(2500, 110)

def create_stones():
    for i in range(1):
        stone = Stone(random.randint(1100,1500),80)

def create_man():
    master = Man(3300,150)

def create_objects():
    global background, cat, zombie, heart, man
    background = BackGround()
    cat = Cat()
    heart = Heart()
    create_lands()
    create_zombies()
    create_stones()
    create_man()

def delete_objects():
    for stone in stones:
        stones.remove(stone)

    for zombie in zombies:
        zombies.remove(zombie)

    for lands in land:
        land.remove(lands)

    for master in man:
        man.remove(master)


# state
def enter():
    #open_canvas(window_width,window_height)
    game_framework.reset_time()
    create_objects()

def exit():
    global background, cat, heart
    delete_objects()
    del(background)
    del(cat)
    del(heart)
    #close_canvas()

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(stageclear_state)
        else:
            cat.handle_event(event)

def update(frame_time):
    global move_frames
    cat.update(frame_time)
    for zombie in zombies:
        zombie.update(frame_time)
        if collide(cat, zombie):
            heart.attacked()
            zombies.remove(zombie)

    for stone in stones:
        if collide(cat, stone):
            heart.attacked()
            #stones.remove(stone)

    for master in man:
        if collide(cat, master):
            cat.stop(master)
            #game_framework.push_state(stageclear_state)

    background.update(frame_time)

    if( heart.state == heart.DIE):
        game_framework.push_state(gameover_state)
    update_canvas()

def draw_main_scene(frame_time):
    global move_frames
    background.draw()
    for lands in land:
        lands.draw()
    cat.draw()

    for stone in stones:
        stone.draw()

    for master in man:
        master.draw()

    heart.draw()
    if move_frames >= 2000:
        for zombie in zombies:
            zombie.draw()

def draw(frame_time):
    clear_canvas()
    draw_main_scene(frame_time)
    update_canvas()





