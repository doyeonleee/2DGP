from pico2d import *

#Create Obstacle

class Stone:
    def __init__(self):
        self.image = load_image('E:\\Data\\2DGP\\Project\\Resourse\\stone.png')

    def draw(self):
        self.image.draw(500,50)