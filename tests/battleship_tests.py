from mock import patch, Mock
from nose.tools import *

from main.battleship import Battlefield, Ship, Fleet
from main.battleship import SHIP_MARKER


def test_battlefield():
    battlefield = Battlefield()
    assert_equal(10, len(battlefield.grid))

    carrier = Ship('carrier', ('B', 3), 'down')
    carrier.coordinates = [('B', 3), 
                           ('B', 4), 
                           ('B', 5), 
                           ('B', 6), 
                           ('B', 7)]
    battlefield.map_ship(carrier)
    assert_equal(SHIP_MARKER, battlefield.grid[3]['B'])



def test_ship():
    destroyer = Ship('destroyer', ('J', 2), 'down')
    assert_equal(2, destroyer.length)

    destroyer.set_coordinates()
    assert_equal([('J', 2), ('J', 3)], destroyer.coordinates)

    carrier = Ship('carrier', ('B', 3), 'down')
    carrier.set_coordinates()
    assert_equal(5, len(carrier.coordinates))


def test_fleet():
    sub1 = Ship('submarine', ('E', 8), 'accross')
    carrier = Ship('carrier', ('B', 3), 'down')
    cruiser = Ship('cruiser', ('G', 6), 'accross')
    destroyer1 = Ship('destroyer', ('J', 2), 'down')
    battleship = Ship('battleship', ('E', 1), 'down')
    sub2 = Ship('submarine', ('J', 10), 'down')
    destroyer2 = Ship('destroyer', ('G', 1), 'accross')

    fleet = Fleet([sub1, carrier, cruiser, destroyer1, 
                   battleship, sub2, destroyer2])

    assert_equal(7, len(fleet.ships))
    assert_equal(18, fleet.health)