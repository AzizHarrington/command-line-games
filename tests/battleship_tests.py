from mock import patch, Mock
from nose.tools import *

from main.battleship import Battlefield, Ship


def test_battlefield():
    battlefield = Battlefield()

    assert_equal(10, len(battlefield.grid))


def test_ship():
    carrier = Ship('destroyer', (8, 'E'), 'accross')

    assert_equal([(8, 'E'), (8, 'F')], carrier.coordinates)