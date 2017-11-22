from pico2d import *

import game_framework
import title_state
import gameover_state

#Create Life
class Heart:
    image = None
    FIRST, SECOND, THIRD, LAST, DIE = 0, 1, 2, 3, 4
    def __init__(self):
        self.x, self.y = 1600, 700
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
        elif (self.state == self.DIE):
            self.image = load_image('gameover.png')
            self.image.draw(900, 450)