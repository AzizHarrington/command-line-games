import random
import sys
import itertools

sys.setrecursionlimit(100000)

SHIP_MARKER = '▣'
HIT = '▢'
ENEMY_HIT = 'X'
ENEMY_MISS = '⚑'
EMPTY = '◠'
ABC = 'ABCDEFGHIJ'
LIMIT = len(ABC)

PLACEFLEET_RECURSE_COUNT = 0

class Ship(object):
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = self.length


class Node(object):
    def __init__(self):
        self.ship = None
        self.hit = False


class GameGrid(object):
    def __init__(self):
        self.points = list(itertools.product(ABC, range(LIMIT)))
        self.grid = {alpha: {num: Node() 
                    for num in range(1, LIMIT + 1)}
                    for alpha in ABC}

    def place_fleet(self, fleet):
        global PLACEFLEET_RECURSE_COUNT
        PLACEFLEET_RECURSE_COUNT += 1
        if len(fleet) == 0:
            print("reached base")
            return True
        else:
            num_points = len(self.points)
            point = None
            if num_points > 0:
                point = self.points.pop(random.randrange(len(self.points)))
            else:
                print("ran out of points to check")
                return True
            ship = fleet[0]
            across = random.randrange(2)
            success = self._place_ship(ship, point, across)
            if success:
                print("recurse")
                return self.place_fleet(fleet[1:])
            else:
                self.points.append(point)
                print("recurse")
                return self.place_fleet(fleet)

    def _place_ship(self, ship, coords, across=1):
        """
        Places a ship within the confines of the grid.
        Also ensures no overlapping or adjacent ships
        """
        x, y = coords
        nodes = []
        for i in range(ship.length):
            # check coords
            try:
                # check surrounding coords
                perimeter = [
                    (chr(ord(x)+1), y),
                    (chr(ord(x)-1), y),
                    (x, y+1),
                    (x, y-1)
                ]
                for c in perimeter:
                    perimeter_node = self.grid[c[0]][c[1]]
                    # check that adjacent perimeter_node
                    # does not contain reference to another ship
                    if perimeter_node.ship and perimeter_node.ship != ship:
                        print("%s placement failed: Adjacent ship" % ship.name)
                        return False
            except KeyError:
                pass
            try:
                # we've made it through the perimeter check,
                # keep track of current node
                node = self.grid[x][y]
            except:
                # key error
                print("%s placement failed: KeyError" % ship.name)
                return False
            if node.ship:
                # node occupied by another ship
                print("%s placement failed: node already contained ship" % ship.name)
                return False
            else:
                nodes.append(node)
            if across:
                # increment x to assign
                # horizontally
                x = chr(ord(x) + 1)
            else:
                # increment y to
                # assign vertically
                y += 1
        for node in nodes:
            node.ship = ship
        print("%s placed successfully!" % ship.name)
        return True

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
                node = self.grid[a][i]
                if node.ship:
                    line += SHIP_MARKER
                else:
                    line += EMPTY
                line += ' '
            #print row and cell
            print(line)


g = GameGrid()

mega_warship = Ship("mega war ship", 6)

super_battleship = Ship("super battleship", 5)

super_battleship2 = Ship("super battleship 2", 5)

battleship = Ship("battleship", 3)

battleship2 = Ship("battleship 2", 3)

battleship3 = Ship("battleship 3", 3)

destroyer = Ship("destroyer", 2)

destroyer2 = Ship("destroyer 2", 2)

destroyer3 = Ship("destroyer 3", 2)

destroyer4 = Ship("destroyer 4", 2)

sub = Ship("submarine", 1)

sub2 = Ship("submarine 2", 1)

carrier = Ship("carrier", 4)

carrier2 = Ship("carrier 2", 4)

fleet = [
    super_battleship,
    carrier,
    carrier2,
    battleship,
    battleship2,
    battleship3,
    destroyer,
    destroyer2,
    destroyer3,
    destroyer4
]

g.place_fleet(fleet)
print("Total recurssive calls to place_fleet: %s" % PLACEFLEET_RECURSE_COUNT)
g.render_grid()

