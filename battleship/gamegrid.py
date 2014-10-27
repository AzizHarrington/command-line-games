import random
import itertools
import copy

class Ship(object):
    """
    Represents ship object on
    game grid
    """
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.health = self.length


class Node(object):
    """
    Nodes are assigned to each coordinate point
    of the game grid, and contain references to
    ships, and information on whether the node
    has been fired upon.
    """
    def __init__(self):
        self.ship = None
        self.hit = False


class GameGrid(object):
    """
    Contains the games grid data structure: a
    dictionary of char and int coordinate pairs 
    (ie: ('A', 1)) containing nodes with references
    to ships.
    Methods for ship placement, rendering, and 
    firing.
    """
    def __init__(self, fleet):
        self.fleet = fleet
        self.fleet_health = sum([s.health for s in self.fleet])
        self.ABC = 'ABCDEFGHIJ'
        self.LIMIT = len(self.ABC)
        self.points = list(itertools.product(self.ABC, range(self.LIMIT)))
        self.grid = {alpha: {num: Node() 
                    for num in range(1, self.LIMIT + 1)}
                    for alpha in self.ABC}

    def fire(self, x, y):
        """
        Method for firing upon grid.
        Takes x (char) and y (int)
        and checks node at (x,y) coordinates

        Returns:
        2 = hit ship
        1 = miss
        0 = node already fired upon
        """
        node = self.grid[x][y]
        # check that node has not yet
        # been hit
        if not node.hit:
            node.hit = True
            if node.ship:
                node.ship.health -= 1
                self.fleet_health -= 1
                return 2
            return 1
        return 0

    def place_fleet(self):
        """
        Recursive function that takes list of 
        ship objects (fleet) and places them 
        randomly into game grid nodes.
        """
        def find_placements(fleet):
            if len(fleet) == 0:
                # simple base case that
                # no ships remain to be placed
                return True
            else:
                num_points = len(self.points)
                point = None
                if num_points > 0:
                    point = self.points.pop(random.randrange(len(self.points)))
                else:
                    # we've run out of points to check
                    # exit recursive loop with return True
                    return True
                ship = fleet[0]
                across = random.randrange(2)
                success = self._place_ship(ship, point, across)
                if success:
                    # recurse with one less ship
                    return find_placements(fleet[1:])
                else:
                    # put the point back;
                    # it may work for placement of
                    # of smaller ship
                    self.points.append(point)
                    # recurse with unchanged fleet
                    return find_placements(fleet)

        fleet = copy.copy(self.fleet)
        find_placements(fleet)

    def _place_ship(self, ship, coords, across=1):
        """
        Places a ship within the confines of the grid.
        Also ensures no overlapping or adjacent ships
        """
        x, y = coords
        nodes = []  # list of valid nodes
        for i in range(ship.length):
            # check coords
            # check surrounding coords
            perimeter = [
                (chr(ord(x)+1), y),
                (chr(ord(x)-1), y),
                (x, y+1),
                (x, y-1)
            ]
            for c in perimeter:
                try:
                    perimeter_node = self.grid[c[0]][c[1]]
                    # check that adjacent perimeter_node
                    # does not contain reference to another ship
                    if perimeter_node.ship and perimeter_node.ship != ship:
                        return False
                except KeyError:
                    pass
            try:
                # we've made it through the perimeter check,
                # keep track of current node
                node = self.grid[x][y]
            except KeyError:
                # key error
                return False
            if node.ship:
                # node occupied by another ship
                return False
            else:
                # add the node to list 
                # for later ship assignment
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
        # ship placement success!
        return True
