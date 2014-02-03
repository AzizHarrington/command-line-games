
#some constants
SHIP_MARKER = '▣'
HIT = '▢'
ENEMY_HIT = 'X'
ENEMY_MISS = '⚑'
EMPTY = '◠'
ABC = 'ABCDEFGHIJ'
LIMIT = len(ABC)


class Battlefield(object):
    """
    Object to represent battlefield grid and
    associated methods.
    """
    def __init__(self):
        """
        Initialize dictionary to represent battlefield grid.
        """
        self.grid = {num: {alpha: EMPTY
                        for alpha in ABC}
                        for num in range(1, LIMIT + 1)}

    def render_grid(self):
        """
        Draw self on command line terminal.
        """
        #make column headers = abc's
        line = '   '
        for a in ABC:
            line += a
            line += ' '
        print(line)
        # add row header and row
        for i in range(1, LIMIT + 1):
            # if row header # is one digit
            # add a space before printing to align with
            # two digit header
            line = ' ' if len(str(i)) == 1 else ''
            # add header (ie '5')
            line += str(i)
            line += ' '
            # add row cells
            for a in ABC:
                line += self.grid[i][a]
                line += ' '
            #print row and cell
            print(line)

    def map_ship(self, ship):
        """
        Takes a ship and loops through its coords
        to add it onto the grid.
        """
        if ship.coordinates:
            for coordinate in ship.coordinates:
                #split up coords into x & y
                x = coordinate[0] # ie 'J'
                y = coordinate[1] # ie 5
                self.grid[y][x] = SHIP_MARKER

    def fire(self, coordinate, fleet):
        """
        Takes coordinate and looks to for 
        a ship at matching poin on grid.
        If there is a ship, register a hit.
        otherwise, miss.
        """
        hit = False
        for ship in fleet.ships:
            if coordinate in ship.coordinates:
                # if ship is at coordinates, decrement 
                # ship health by 1
                ship.health -= 1
                hit = True
        x = coordinate[0]
        y = coordinate[1]
        if hit:
            self.grid[y][x] = ENEMY_HIT
            return True
        else:
            self.grid[y][x] = ENEMY_MISS
            return False


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


class Fleet(object):
    def __init__(self, ships):
        self.ships = ships
        self.health = sum([ship.length for ship in self.ships])


battlefield = Battlefield()


sub1 = Ship('submarine', ('E', 8), 'accross')
carrier = Ship('carrier', ('B', 3), 'down')
cruiser = Ship('cruiser', ('G', 6), 'accross')
destroyer1 = Ship('destroyer', ('J', 2), 'down')
battleship = Ship('battleship', ('E', 1), 'down')
sub2 = Ship('submarine', ('J', 10), 'down')
destroyer2 = Ship('destroyer', ('G', 1), 'accross')

fleet = Fleet([sub1, carrier, cruiser, destroyer1, battleship, sub2, destroyer2])


for ship in fleet.ships:
    ship.set_coordinates()
    # print(ship.coordinates)
    battlefield.map_ship(ship)

battlefield.render_grid()



# while True:
#     battlefield.render_grid()
#     coords = input('Enter coords > ')
#     if coords == "n":
#         break
#     x, y = coords[0], int(coords[1])
#     battlefield.fire((x, y), fleet)




