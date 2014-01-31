
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
        for i in range(ship.length):
            if ship.direction == 'accross':
                self.grid[ship.x][chr(ord(ship.y) + i)] = SHIP_MARKER
            elif ship.direction == 'down':
                self.grid[ship.x + i][ship.y] = SHIP_MARKER


class Ship(object):
    ship_length = {'carrier': 5,
                   'battleship': 4,
                   'cruiser': 3,
                   'destroyer': 2,
                   'submarine': 1}

    def __init__(self, name, pos, direction):
        self.name = name
        self.length = self.ship_length[name]
        self.direction = direction
        self.x = pos[0]
        self.y = pos[1]


battlefield = Battlefield()

battlefield.render_grid()

sub1 = Ship('submarine', (8, 'E'), 'accross')
carrier = Ship('carrier', (3, 'B'), 'down')
cruiser = Ship('cruiser', (6, 'G'), 'accross')
destroyer1 = Ship('destroyer', (2, 'J'), 'down')
battleship = Ship('battleship', (1, 'E'), 'down')
sub2 = Ship('submarine', (10, 'J'), 'down')
destroyer2 = Ship('destroyer', (1, 'G'), 'accross')

fleet = [sub1, carrier, cruiser, destroyer1,
         battleship, sub2, destroyer2]

for ship in fleet:
    battlefield.map_ship(ship)

battlefield.render_grid()

print(battlefield.grid)
