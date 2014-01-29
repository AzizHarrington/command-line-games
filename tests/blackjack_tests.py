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
    player = Player()

    player.deal(['4♠', '7♦'])
    assert_equal(player.hand, ['4♠', '7♦'])

    player.hit(['T♣'])
    assert_equal(player.hand, ['4♠', '7♦', 'T♣'])

    #TODO
    #commented methods below need input() to be mocked

    #player.next_move()

    #player.current_score()

    ten_value = player.value('T♠')
    assert_equal(ten_value, 10)

    num_value = player.value('7♣')
    assert_equal(num_value, 7)

    #get_ace_value()


def test_dealer():
    pass


def test_game():
    pass