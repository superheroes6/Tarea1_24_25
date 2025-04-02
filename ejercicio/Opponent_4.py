from Character_2 import Character
from Shot_5 import Shot

class Opponent(Character):
    def __init__(self, x, y, image, is_star=False):
        super().__init__(x, y, image, 3)
        self.is_star = is_star

    def move(self, dx, dy):
        super().move(dx, dy)

    def shoot(self):
        shot = Shot(self.x, self.y + 1, "enemy_bullet.png", 3)
        print(f"{self} shoots!")
        return shot

    def collide(self, other):
        if isinstance(other, Shot):
            self.is_alive = False
            other.owner.score += 1
            print(f"Opponent hit! Score: {other.owner.score}")
