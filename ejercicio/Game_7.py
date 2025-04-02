from Player_3 import Player
from Opponent_4 import Opponent
from Boss_6 import Boss

class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")

    def end_game(self):
        if isinstance(self.opponent, Boss) and self.player.lives > 0:
            print("Congratulations! You defeated the final boss and won the game!")
        else:
            print("Game ended!")
        self.is_running = False

    def reset(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False
        print("Game has been reset.")

    def initialize_player(self, player_name):
        self.player = Player(0, 0, "player_image.png", name=player_name)
        print(f"Player {self.player.name} initialized with {self.player.lives} lives.")

    def spawn_opponent(self):
        self.opponent = Opponent(10, 10, "enemy_image.png")
        print("Opponent spawned!")

    def spawn_boss(self):
        self.opponent = Boss(10, 10, "boss_image.png")
        print("A boss has appeared!")

    def update_score_and_lives(self):
        print(f"Score: {self.score}, Lives: {self.player.lives}")
