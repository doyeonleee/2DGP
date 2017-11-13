from pico2d import *

class Stage1:
        def __init__(self):
            self.image = load_image('Main_BackGround.png')

        def draw(self):
            self.image.draw(500, 300)