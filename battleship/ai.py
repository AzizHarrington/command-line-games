import random

class OpponentAi(object):
    def __init__(self):
        pass

    def choose_coords(self, grid):
        x = random.sample(grid.ABC, 1)
        y = random.randint(1, grid.LIMIT)

        return "%s%s" % (x[0], y)