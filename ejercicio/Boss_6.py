from Opponent_4 import Opponent

class Boss(Opponent):
    def __init__(self, x, y, image, is_star=False, speed_multiplier=2):
        super().__init__(x, y, image, is_star)
        self.speed_multiplier = speed_multiplier

    def move(self, dx, dy):
        super().move(dx * self.speed_multiplier, dy * self.speed_multiplier)
