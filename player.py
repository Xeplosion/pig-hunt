# Foster Cavender
# CS1400 online 7 week

class Player:
    def __init__(self, image):
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.radius = self.width / 2 - 1
        self.center_x = 300
        self.center_y = 450
        self.draw_x = self.center_x - self.width / 2
        self.draw_y = self.center_y - self.height / 2

    def set_draw_pos(self):
        # set the draw pos based off player asset dimensions
        self.draw_x = self.center_x - self.width / 2
        self.draw_y = self.center_y - self.height / 2

    def check_offscreen(self):
        # check if player pos is offscreen
        if self.draw_x < 0 or self.draw_y < 0:
            return True
        elif self.draw_x > 600 - self.width or self.draw_y > 600 - self.height:
            return True
        else:
            return False

    def move_player(self, move):
        # move player, then move back if offscreen
        self.center_x += move[0]
        self.set_draw_pos()
        if self.check_offscreen():
            self.center_x -= move[0]
        self.center_y += move[1]
        self.set_draw_pos()
        if self.check_offscreen():
            self.center_y -= move[1]

    def reset(self):
        self.center_x = 300
        self.center_y = 450
        self.set_draw_pos()

