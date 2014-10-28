import os

from gamegrid import Ship, GameGrid

SHIP_MARKER = '▣'
HIT = '▢'
ENEMY_HIT = 'X'
ENEMY_MISS = '⚑'
EMPTY = '◠'


def render_grid(grid):
    """
    Draw grid on command line terminal.
    """
    #make column headers = abc's
    line = '   '
    for a in grid.ABC:
        line += a
        line += ' '
    print(line)
    # add row header and row
    for i in range(1, grid.LIMIT + 1):
        # if row header # is one digit
        # add a space before printing to align with
        # two digit header
        line = ' ' if len(str(i)) == 1 else ''
        # add header (ie '5')
        line += str(i)
        line += ' '
        # add row cells
        for a in grid.ABC:
            node = grid.grid[a][i]
            if node.ship:
                if node.hit:
                    line += HIT
                else:
                    line += SHIP_MARKER
            else:
                if node.hit:
                    line += ENEMY_MISS
                else:
                    line += EMPTY
            line += ' '
        #print row and cell
        print(line)


def fire_shot(coords, board):
    """
    Check's that coordinates are correct format, and
    prints results of shot.
    Returns True if coordinates are valid, otherwise False.
    """
    try:
        # unpack coord string
        x, y = coords
        x = x.upper()
        y = int(y)

    except ValueError:
        print("Invalid coordinates. Please type letter first, then number.")
        return False

    if x not in board.ABC or y > board.LIMIT:
        print("Coordinates out of range. Try again.")
        return False

    result = board.fire(x, y)

    if result == 2:
        ship = board.grid[x][y].ship
        print("Hit on opponent's %s" % ship.name)
        if ship.health == 0:
            print("You've sunk the enemy %s!" % ship.name)
        return True

    elif result == 1:
        print("Miss!")
        return True

    elif result == 0:
        print("You've already fired at those coordinates, try again.")
        return False


fleet = [
    Ship("Aircraft Carrier", 5),
    Ship("Battleship", 4),
    Ship("Cruiser", 3),
    Ship("Destroyer", 2),
    Ship("Destroyer", 2),
    Ship("Submarine", 1),
    Ship("Submarine", 1),
]

clear = lambda: os.system('clear')

def main():
    opponent = GameGrid(fleet)
    defending_player = GameGrid(fleet)
    opponent.place_fleet()
    defending_player.place_fleet()

    clear()
    print("Welcome to Battleship: command line edition!")
    print("Press enter to start the game")
    input(">")

    player_turn = True
    game_won = False
    times_through_loop = 0

    while not game_won:
        clear()
        print("Times through loop: %s" % times_through_loop)
        times_through_loop += 1
        print("Oppenent's board:")
        render_grid(opponent)
        print()
        print("Your board:")
        render_grid(defending_player)
        print()

        if player_turn:
            print("Enter coordinates to launch attack on opponent!")
            print("(ex: 'b4')")
            hit = False

            while not hit:
                coords = input()
                hit = fire_shot(coords, opponent)

        print("Opponent fleet health: %s" % opponent.fleet_health)

        if opponent.fleet_health == 0:
            print("Congratulations, you've destroyed the enemy fleet!")
            print("You win!")
            break

        input("continue.. >")


main()



















