# Foster Cavender
# CS1400 online 7 week

import drawly
import math
class Moody:
    def __init__(self, start_smile, start_happy, start_dark_eyes):
        self.smile = start_smile
        self.happy = start_happy
        self.dark_eyes = start_dark_eyes

    def draw_head(self):
        if self.happy:
            drawly.set_color("yellow")
        else:
            drawly.set_color("red")
        drawly.circle(700, 300, 200)
        drawly.set_color("black")
        drawly.circle(700, 300, 200, 5)
    def draw_eyes(self):
        if self.dark_eyes:
            drawly.set_color("black")
        else:
            drawly.set_color("green")
        drawly.circle(625, 275, 20)
        drawly.circle(775, 275, 20)
    def draw_mouth(self):
        drawly.set_color("black")
        if self.happy:
            drawly.arc(600, 325, 200, 75, 200, 340, 10)
        else:
            drawly.arc(600, 375, 200, 75, 20, 160, 10)

    def draw_face(self):
        self.draw_head()
        self.draw_eyes()
        self.draw_mouth()
        drawly.redraw()

    def is_smile(self):
        return self.smile

    def is_happy(self):
        return self.happy

    def is_dark_eyes(self):
        return self.dark_eyes

    def change_mouth(self):
        self.smile = False if self.smile else True

    def change_emotion(self):
        self.happy = False if self.happy else True

    def change_eyes(self):
        self.dark_eyes = False if self.dark_eyes else True
