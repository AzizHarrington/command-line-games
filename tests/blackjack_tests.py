from nose.tools import *

from main.blackjack import Deck, Hand


def test_deck():
    deck = Deck()
    assert_equal(len(deck.cards), 52)

    deck.dealtwo()
    deck.dealone()
    assert_equal(len(deck.cards), 49)

# suites: ♠♥♦♣
def test_hand():
    hand = Hand(['T♠', '2♥'])
    assert_equal(hand.cards, ['T♠', '2♥'])

    hand.update(['T♣'])
    assert_equal(hand.cards, ['T♠', '2♥', 'T♣'])
    assert_equal(hand.score(), 'Bust!')

    hand = Hand(['K♠', 'T♣'])
    assert_equal(hand.score(), 20)

# def test_hand_w_user_input():
#     hand = Hand(['A♥', 'J♠'])
#     assert_equal(hand.score(), 'Blackjack!')

