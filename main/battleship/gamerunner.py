from gamegrid import Ship, Node, GameGrid

player1 = GameGrid()
player2 = GameGrid()

fleet = [
    Ship("Aircraft Carrier", 5),
    Ship("Battleship", 4),
    Ship("Cruiser", 3),
    Ship("Destroyer", 2),
    Ship("Destroyer", 2),
    Ship("Submarine", 1),
    Ship("Submarine", 1)
]

player1.place_fleet(fleet)
player2.place_fleet(fleet)
player2.render_grid()
player1.render_grid()
