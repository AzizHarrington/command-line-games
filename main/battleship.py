
#some constants
SHIP_MARKER = '▣'
HIT = '▢'
ENEMY_HIT = 'X'
ENEMY_MISS = 'O'
EMPTY = '◠'
ABC = 'ABCDEFGHIJ'
LIMIT = len(ABC)


class Battlefield(object):
    def __init__(self):
        self.grid = {num: {alpha: EMPTY
                        for alpha in ABC}
                        for num in range(1, LIMIT + 1)}

    def display_grid(self):
        line = '   '
        for a in ABC:
            line += a
            line += ' '
        print(line)

        for i in range(1, LIMIT + 1):
            line = ' ' if len(str(i)) == 1 else ''
            line += str(i)
            line += ' '
            for a in ABC:
                line += self.grid[i][a]
                line += ' '
            print(line)


class Ship(object):
    ship_length = {'carrier': 5,
                   'battleship': 4,
                   'cruiser': 3,
                   'destroyer': 2,
                   'submarine': 1}

    def __init__(self, name, pos, direction):
        self.name = name
        self.direction = direction
        self.x = pos[0]
        self.y = pos[1]

    def render(self, ship):
        length = self.ship_length[self.name]
        for i in range(length):
            if self.direction == 'accross':
                grid.grid[self.x][chr(ord(self.y) + i)] = SHIP_MARKER
            elif self.direction == 'down':
                grid.grid[self.x + i][self.y] = SHIP_MARKER


grid = Battlefield()

sub1 = Ship('submarine', [8, 'E'], 'accross')
carrier = Ship('carrier', [3, 'B'], 'down')
cruiser = Ship('cruiser', [6, 'G'], 'accross')
destroyer1 = Ship('destroyer', [2, 'J'], 'down')
battleship = Ship('battleship', [1, 'E'], 'down')
sub2 = Ship('submarine', [10, 'J'], 'down')
destroyer2 = Ship('destroyer', [1, 'G'], 'accross')

sub1.render(grid)
carrier.render(grid)
cruiser.render(grid)
destroyer1.render(grid)
battleship.render(grid)
sub2.render(grid)
destroyer2.render(grid)

grid.display_grid()