from pico2d import *

#Create Stage

class Stage1:
        def __init__(self):
            self.image = load_image('stage1.png')

        def draw(self):
            self.image.draw(900, 450)