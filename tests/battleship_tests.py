from mock import patch, Mock
from nose.tools import *

from main.battleship import Battlefield, Ship


def test_battlefield():
    battlefield = Battlefield()

    assert_equal(10, len(battlefield.grid))


def test_ship():
    destroyer = Ship('destroyer')
    assert_equal(2, destroyer.length)

    destroyer.set_coordinates(('E', 8), 'accross')
    assert_equal([('E', 8), ('F', 8)], destroyer.coordinates)

    carrier = Ship('carrier')
    carrier.set_coordinates(('B', 3), 'down')
    assert_equal(5, len(carrier.coordinates))