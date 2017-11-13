from pico2d import *

class Heart:
    def __init__(self):
        self.image =load_image('E:\\Data\\2DGP\\Project\\Resourse\\Heart_FULL.png')

    def draw(self):
        self.image.draw(900,500)