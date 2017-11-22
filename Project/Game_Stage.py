from pico2d import *

#Create Stage


class Create_Stage:
    pass


class Stage1:
    def __init__(self):
        self.image = load_image('stage_1.png')

    def draw(self):
        self.image.draw(900, 450)

    def get_bb(self):
        pass

    def draw_bb(self):
        pass

