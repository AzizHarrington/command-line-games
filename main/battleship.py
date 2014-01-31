
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

    def render_grid(self):
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

    def map_ship(self, ship):
        if ship.coordinates:
            for coordinate in ship.coordinates:
                x = coordinate[0] # ie 'J'
                y = coordinate[1] # ie 5
                self.grid[y][x] = SHIP_MARKER


class Ship(object):
    ship_length = {'carrier': 5,
                   'battleship': 4,
                   'cruiser': 3,
                   'destroyer': 2,
                   'submarine': 1}

    def __init__(self, name, pos, direction):
        self.name = name
        self.pos = pos
        self.direction = direction
        self.length = self.ship_length[name]
        self.coordinates = None

    def set_coordinates(self):
        coordinates = []
        x = self.pos[0] # ie 'J'
        y = self.pos[1] # ie 5
        for i in range(self.length):
            if self.direction == 'accross':
                coordinate = (chr(ord(x) + i), y)
            elif self.direction == 'down':
                coordinate = (x, y + i)
            coordinates += [coordinate]
        self.coordinates = coordinates




battlefield = Battlefield()

# battlefield.render_grid()

sub1 = Ship('submarine', ('E', 8), 'accross')
carrier = Ship('carrier', ('B', 3), 'down')
cruiser = Ship('cruiser', ('G', 6), 'accross')
destroyer1 = Ship('destroyer', ('J', 2), 'down')
battleship = Ship('battleship', ('E', 1), 'down')
sub2 = Ship('submarine', ('J', 10), 'down')
destroyer2 = Ship('destroyer', ('G', 1), 'accross')

fleet = [sub1, carrier, cruiser, destroyer1,
         battleship, sub2, destroyer2]

for ship in fleet:
    ship.set_coordinates()
    battlefield.map_ship(ship)

battlefield.render_grid()

# print(battlefield.grid)
