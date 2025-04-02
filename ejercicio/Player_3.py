from Character_2 import Character
from Shot_5 import Shot

class Player(Character):
    def __init__(self, x, y, image, score=0, lives=3):
        super().__init__(x, y, image, lives)
        self.score = score

    def move(self, dx, dy):
        super().move(dx, dy)

    def shoot(self):
        shot = Shot(self.x, self.y - 1, "bullet_image.png", 5)
        print(f"{self} shoots!")
        return shot

    def collide(self, other):
        if isinstance(other, Shot):
            self.lives -= 1
            print(f"Player hit! Lives remaining: {self.lives}")
            if self.lives <= 0:
                self.is_alive = False
                print("Game Over!")
