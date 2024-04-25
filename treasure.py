# Foster Cavender
# CS1400 online 7 week

import random


class Treasure:
    def __init__(self, image):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width / 2 - 1
        self.center_x = random.randint(0 + self.width / 2, 600 - self.width / 2)
        self.center_y = random.randint(0 + self.height / 2, 600 - self.height / 2)
        self.draw_x = self.center_x - self.width / 2
        self.draw_y = self.center_y - self.height / 2