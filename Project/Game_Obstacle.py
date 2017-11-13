from pico2d import *

class Stone:
    def __init__(self):
        self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\stone.png')

    def draw(self):
        self.image.draw(900,50)