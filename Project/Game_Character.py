from pico2d import *

class Cat:
    image = None
    LEFT_RUN, RIGHT_RUN, LEFT_IDLE, RIGHT_IDLE = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.state = self.RIGHT_IDLE

    #RUN = 8, IDLE = 10
    def update(self):
        if self.state in (self.RIGHT_IDLE, self.LEFT_IDLE):
            self.frame = (self.frame +1) % 10
        elif self.state in (self.RIGHT_RUN, self.LEFT_RUN):
            self.frame = (self.frame + 1) % 8

        if self.state == self.RIGHT_RUN:
            self.x = min(1000,self.x + 5)
        elif self.state == self.LEFT_RUN:
            self.x = max(0, self.x -5)

    def draw(self):
        if self.state == self.RIGHT_IDLE:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_Right_Idle2.png')
                self.image.clip_draw(self.frame * 98, 0, 100, 100, self.x, self.y)
        elif self.state == self.LEFT_IDLE:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_LEFT_Idle2.png')
                self.image.clip_draw(self.frame * 98, 0, 100, 100, self.x, self.y)
        elif self.state == self.RIGHT_RUN:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_Right_RUN.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 101, self.x, self.y)
        elif self.state == self.LEFT_RUN:
            if Cat.image == None:
                self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\Cat_LEFT_RUN.png')
                self.image.clip_draw(self.frame * 100, 0, 100, 101, self.x, self.y)

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