import random


class Deck(object):

    def __init__(self):
        self.cards = ['%s%s' % (num, suit)
                      for num in 'A23456789TJQK'
                      for suit in '♠♥♦♣']
        random.shuffle(self.cards)

    def drawone(self):
        if len(self.cards) == 0:
            print("everyday i'm shufflin'....")
            self.__init__()
        return [self.cards.pop()]

    def drawtwo(self):
        return self.drawone() + self.drawone()


deck = Deck()


class Player(object):

    def __init__(self):
        self.hand = None
        self.stay = False

    def deal(self):
        self.hand = deck.drawtwo()

    def hit(self): #accepts list as input
        self.hand.extend(deck.drawone())

    def next_move(self):
        print("What would you like to do next? (choose one)")
        print("Take a hit: 1")
        print("Stay: 2")
        print("Look at hand: 3")
        next = input(">")
        if next == '1':
            self.hit()
        elif next == '2':
            self.stay = True
        elif next == '3':
            print(self.hand)
            self.next_move()
        else:
            print("Please enter 1, 2, or 3")
            self.next_move()

    def current_score(self):
        score = 0
        for card in self.hand:
            if card[0] != 'A':
                score += self.value(card)
        for card in self.hand:
            if card[0] == 'A':
                score += self.get_ace_value(card, score)
        if (score == 21) and (len(self.hand) == 2) and ('J♣' or 'J♠' in self.hand):
            return 22
            print("Blackjack!")
        elif score > 21:
            return 0
            print("Bust!")
        else:
            return score

    def value(self, card):
        number = card[0]
        if number in 'TJQK':
            return 10
        else:
            return int(number)

    def get_ace_value(self, card, score):
        print("Current score is: %s" % (score,))
        print("Count '%s' as 1 or 11?" % (card,))
        val = input(">")
        return int(val)


class Dealer(Player):

    def next_move(self):
        if self.current_score() < 17:
            self.hit()
            print("The dealer took a hit.")
        else:
            self.stay = True
            print("The dealer decided to stay.")
    
    def get_ace_value(self, card, score):
        if score <= 10:
            return 11
        else:
            return 1


class Game(object):
    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()

    def play(self):
        print("------------------------------------------------")
        print("Welcome to Command Line Blackjack!")
        print("------------------------------------------------")
        print("Press enter to start the game!")
        input(">")
        print("The dealer begins to shuffle the cards...")
        self.dealer.deal()
        self.player.deal()
        input(">")
        print("...and deals the hands.")
        input(">")
        print("------------------------------------------------")
        print("Dealer:")
        print(self.dealer.hand)
        print("------------------------------------------------")
        input(">")
        print("Your hand:")
        print(self.player.hand)
        print("------------------------------------------------")
        input(">")

        while not (self.dealer.stay and self.player.stay):
            self.dealer.next_move()
            if self.dealer.current_score() == 0:
                print("The dealer busted!")
                print(self.dealer.hand)
                break
            elif self.dealer.current_score() == 22:
                print("The dealer got blackjack!")
                print(self.dealer.hand)
                break
            if not self.dealer.stay:
                print("Dealer:")
                print(self.dealer.hand)
                print("------------------------------------------------")
                input(">")
            self.player.next_move()
            if self.player.current_score() == 0:
                print("You busted!!")
                print(self.player.hand)
                break
            elif self.player.current_score() == 22:
                print("You got blackjack!")
                print(self.player.hand)
                break
            if not self.player.stay:
                print("Your hand:")
                print(self.player.hand)
                print("------------------------------------------------")

        if self.dealer.current_score() >= self.player.current_score():
            print("The house wins. Better luck next time!")
        else:
            print("You win!")


if __name__ == "__main__":
    game = Game()
    game.play()

    print("Play again? (yes/no)")
    again = input(">")
    while again == "yes":
        game = Game()
        game.play()
        print("Play again? (yes/no)")
        again = input(">")
    print("Come back soon.")
