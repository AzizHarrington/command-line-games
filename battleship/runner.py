import os

from .gamegrid import Ship, GameGrid
from .display import render_grid



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
    render_grid(player2)
    render_grid(player1)


main()