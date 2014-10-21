from mock import patch, Mock
from nose.tools import *

from main.blackjack import Deck, Player, Dealer


def test_deck():
    deck = Deck()
    assert_equal(52, len(deck.cards))

    deck.drawtwo()
    deck.drawone()
    assert_equal(49, len(deck.cards))

    for i in range(53):
        deck.drawone()
    assert_equal(True, (len(deck.cards) != 0))

# suites: ♠♥♦♣
def test_player():
    player = Player()

    player.deal()
    assert_equal(2, len(player.hand))

    player.hit()
    assert_equal(3, len(player.hand))

    ten_value = player.value('T♠')
    assert_equal(10, ten_value)

    num_value = player.value('7♣')
    assert_equal(7, num_value)


@patch('builtins.input', lambda x: '1')
def test_player_next_move_is_hit():
    player = Player()
    player.deal()
    player.next_move()
    assert_equal(3, len(player.hand))


@patch('builtins.input', lambda x: '2')
def test_player_next_move_is_stay():
    player = Player()
    player.deal()
    player.next_move()
    assert_equal(True, player.stay)

@patch('builtins.input', lambda x: '11')
def test_player_current_score_with_ace():
    player = Player()
    player.hand = ['J♣', 'A♥']
    player.get_current_score()
    assert_equal(22, player.score)

@patch('builtins.input', lambda x: '11')
def test_player_w_mocked_input():
    player = Player()
    val = player.get_ace_value('A♠', 10)
    assert_equal(11, val)


def test_dealer(): #ai tests
    dealer = Dealer()

    #score two face cards
    dealer.hand = ['J♥', 'Q♠']
    dealer.get_current_score()
    assert_equal(20, dealer.score)

    #score large hand
    dealer.hand = ['2♠', '5♦', '7♥', '2♣']
    dealer.get_current_score()
    assert_equal(16, dealer.score)

    #score two aces
    dealer.hand = ['A♣', 'A♣']
    dealer.get_current_score()
    assert_equal(12, dealer.score)

    #score blackjack
    dealer.hand = ['J♣', 'A♥']
    dealer.get_current_score()
    assert_equal(22, dealer.score)

    #score bust
    dealer.hand = ['T♥', '6♥', 'K♥']
    dealer.get_current_score()
    assert_equal(0, dealer.score)

    #next move under 17
    dealer.hand = ['4♠', '7♦']
    dealer.next_move()
    assert_equal(3, len(dealer.hand))

    #next move 17
    dealer.hand = ['T♥', '7♥']
    dealer.next_move()
    assert_equal(2, len(dealer.hand))
