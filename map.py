import random

class Map:
    def __init__(self):
        self.state=[1,0]
        self.game_map = []

    def generate_map(self, rows, cols):
        self.game_map = []
        for i in range(rows):
            row = []
            for j in range(cols):
                choice = random.choice(self.state)
                row.append(choice)
            self.game_map.append(row)
        return self.game_map

