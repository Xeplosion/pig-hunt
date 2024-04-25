# Foster Cavender
# CS1400 online 7 week

import math
class Enemy:
    def __init__(self, image):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width / 2 - 1
        self.center_x = 300
        self.center_y = 50
        self.draw_x = self.center_x - self.width / 2
        self.draw_y = self.center_y - self.height / 2
        self.move = [15, 80, 80 * (math.pi / 180)]

    def set_draw_pos(self):
        # set the draw pos based off player asset dimensions
        self.draw_x = self.center_x - self.width / 2
        self.draw_y = self.center_y - self.height / 2

    def offscreen(self):
        if self.draw_x < 0:
            return [True, 0]
        if self.draw_y < 0:
            return [True, 180]
        if self.draw_x > 600 - self.width:
            return [True, 0]
        if self.draw_y > 600 - self.height:
            return [True, 180]
        else:
            return [False, 0]

    def move_enemy(self):
        # move enemy, then bounce if offscreen
        self.center_x += math.sin(self.move[2]) * self.move[0]
        self.center_y += math.cos(self.move[2]) * self.move[0]
        bounce = False

        # handle bounces
        if self.offscreen()[0]:
            self.center_x -= math.sin(self.move[2]) * self.move[0]
            self.center_y -= math.cos(self.move[2]) * self.move[0]
            self.move[1] += self.offscreen()[1] - self.move[1] * 2
            self.move[2] = self.move[1] * (math.pi / 180)
            self.center_x += math.sin(self.move[2]) * self.move[0]
            self.center_y += math.cos(self.move[2]) * self.move[0]
            bounce = True

        self.set_draw_pos()
        return bounce

    def reset(self):
        self.center_x = 50
        self.center_y = 300
        self.set_draw_pos()

