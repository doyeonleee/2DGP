import gameover_state

from pico2d import *
from global_values import window_width, window_height



class Heart:
    FIRST, SECOND, THIRD, LAST, DIE = 0, 1, 2, 3, 4

    def __init__(self):
        self.x, self.y = 1400, 500
        self.image = None
        self.state = self.FIRST

    def attacked(self):
        self.state += 1

    def draw(self):
        if (self.state == self.FIRST):
            self.image = load_image('Resources\Life\Heart_Full.png')
            self.image.draw(self.x, self.y)
        elif (self.state == self.SECOND):
            self.image = load_image('Resources\Life\Heart_Attacked_1.png')
            self.image.draw(self.x, self.y)
        elif (self.state == self.THIRD):
            self.image = load_image('Resources\Life\Heart_Attacked_2.png')
            self.image.draw(self.x, self.y)
        elif (self.state == self.LAST):
            self.image = load_image('Resources\Life\Heart_Die.png')
            self.image.draw(self.x, self.y)