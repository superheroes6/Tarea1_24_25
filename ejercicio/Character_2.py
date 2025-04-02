from Entity_1 import Entity

class Character(Entity):
    def __init__(self, x, y, image, lives):
        super().__init__(x, y, image)
        self.lives = lives
        self.is_alive = True

    def move(self, dx, dy):
        super().move(dx, dy)

    def shoot(self):
        pass

    def collide(self, other):
        pass

    def reset(self):
        self.lives = 3
        self.is_alive = True
