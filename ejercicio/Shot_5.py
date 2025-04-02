from Entity_1 import Entity

class Shot(Entity):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image)
        self.speed = speed
        self.is_alive = True

    def move(self):
        self.y -= self.speed

    def hit_target(self):
        pass

    def reset(self):
        self.is_alive = True
        self.x = 0
        self.y = 0
        self.speed = 0
