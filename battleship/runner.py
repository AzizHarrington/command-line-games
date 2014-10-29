import os
import time

from gamegrid import Ship, GameGrid
from ai import OpponentAi

SHIP_MARKER = '▣'
HIT = 'X'
MISS = '⚑'
EMPTY = '◠'


def render_grid(grid, enemy=False):
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
                elif not enemy:
                    line += SHIP_MARKER
                else:
                    line += EMPTY
            else:
                if node.hit:
                    line += MISS
                else:
                    line += EMPTY
            line += ' '
        # print row and cell
        print(line)


def fire_shot(coords, board):
    """
    Check's that coordinates are correct format, and
    prints results of shot.
    Returns True if coordinates are valid, otherwise False.
    """
    try:
        # unpack coord string
        x, y = coords[0], coords[1:]
        x = x.upper()
        y = int(y)

    except:
        print("Invalid coordinates. Please type letter first, then number.")
        print("(ex: 'b4')")
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
        return False

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
    player_board = GameGrid(fleet)
    opponent_board = GameGrid(fleet)
    player_board.place_fleet()
    opponent_board.place_fleet()

    opponent_ai = OpponentAi()

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
        render_grid(opponent_board, enemy=True)
        print()
        print("Your board:")
        render_grid(player_board)
        print()

        if player_turn:
            print("Your turn:")
            print("Enter coordinates to launch attack on opponent!")
            
            hit = False
            while not hit:
                coords = input()
                hit = fire_shot(coords, opponent_board)

            print("Opponent fleet health: %s" % opponent_board.fleet_health)

            if opponent_board.fleet_health == 0:
                print("Congratulations, you've destroyed the enemy fleet!")
                print("You win!")
                break

            player_turn = False

        else:
            print("Opponent's turn.")
            time.sleep(5)

            hit = False
            while not hit:
                coords = opponent_ai.choose_coords(player_board)
                hit = fire_shot(coords, player_board)

            if player_board.fleet_health == 0:
                print("You lose, better luck next time!")

            player_turn = True

        input()


main()



















