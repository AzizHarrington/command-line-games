import os

from gamegrid import Ship, GameGrid

SHIP_MARKER = '▣'
HIT = '▢'
ENEMY_HIT = 'X'
ENEMY_MISS = '⚑'
EMPTY = '◠'

fleet = [
    Ship("Aircraft Carrier", 5),
    Ship("Battleship", 4),
    Ship("Cruiser", 3),
    Ship("Destroyer", 2),
    Ship("Destroyer", 2),
    Ship("Submarine", 1),
    Ship("Submarine", 1)
]

clear = lambda: os.system('clear')

def main():
    clear()
    player1 = GameGrid()
    player2 = GameGrid()
    player1.place_fleet(fleet)
    player2.place_fleet(fleet)
    player2.render_grid()
    player1.render_grid()


main()