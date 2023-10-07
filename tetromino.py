import random

choices = ["I", "O", "T", "J", "L", "S", "Z"]
drawing_matrix = []

# A active tetromino is the tetromino which you can interact with and that falls.

class ActiveTetromino():
    def __init__(self):
        self.position = (random.randint(0, 10), 20)
        self.kind = random.choice(choices)
        # Zero here is just a placeholder
        self.falling_distance = 0

    def rotate_right():
        pass

    def rotate_left():
        pass

    def move_right(self):
        self.position[0] += 1

    def move_left(self):
        self.position[0] -= 1

    def fall(self, input):
        # For the normal falling (gravity).
        if input == 0:
            self.position[1] -= 1
        # For "hard falling (with the space key)"
        elif input == 1:
            self.position[1] -= self.falling_distance