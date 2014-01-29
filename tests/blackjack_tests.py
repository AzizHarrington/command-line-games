from nose.tools import *

from main.blackjack import Deck, Player, Dealer, Game


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

    #TODO
    #commented methods below need input() to be mocked

    #player.next_move()

    #player.current_score()

    ten_value = player.value('T♠')
    assert_equal(10, ten_value)

    num_value = player.value('7♣')
    assert_equal(7, num_value)

    #get_ace_value()


def test_dealer(): #ai tests
    dealer = Dealer()

    #score two face cards
    dealer.hand = ['J♥', 'Q♠']
    score = dealer.current_score()
    assert_equal(20, score)

    #score large hand
    dealer.hand = ['2♠', '5♦', '7♥', '2♣']
    score = dealer.current_score()
    assert_equal(16, score)

    #score two aces
    dealer.hand = ['A♣', 'A♣']
    score = dealer.current_score()
    assert_equal(12, score)

    #score blackjack
    dealer.hand = ['J♣', 'A♥']
    score = dealer.current_score()
    assert_equal(22, score)

    #score bust
    dealer.hand = ['T♥', '6♥', 'K♥']
    score = dealer.current_score()
    assert_equal(0, score)

    #next move under 17
    dealer.hand = ['4♠', '7♦']
    dealer.next_move()
    assert_equal(3, len(dealer.hand))

    #next move 17
    dealer.hand = ['T♥', '7♥']
    dealer.next_move()
    assert_equal(2, len(dealer.hand))


def test_game():
    pass