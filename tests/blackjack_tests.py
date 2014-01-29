from nose.tools import *

from main.blackjack import Deck, Player, Dealer, Game


def test_deck():
    deck = Deck()
    assert_equal(len(deck.cards), 52)

    deck.drawtwo()
    deck.drawone()
    assert_equal(len(deck.cards), 49)

    for i in range(53):
        deck.drawone()
    assert_equal(True, (len(deck.cards) != 0))


# suites: ♠♥♦♣
def test_player():
    pass


def test_dealer():
    pass


def test_game():
    pass