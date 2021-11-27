import random

class Cards:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def face(self):
        return (self.suit, self.value)

def new_deck():
    suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    values = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck = []
    for s in suits:
        for v in values:
            c = Cards(s, v)
            deck.append(Cards.face(c))
    return deck


def new_card(hand, deck):
    i = random.choice(range(len(deck)))
    hand.append(deck[i])
    deck.pop(i)


def score_calc(h):
    score = 0
    ace_count = 0
    for card in h:
        if card[1] == 'A':
            ace_count += 1
        elif card[1] == 'J' or card[1] == 'Q' or card[1] == 'K':
            score += 10
        else:
            score += card[1]
    while ace_count > 0:
        if score + 11 < 21:
            score += 11
            ace_count -= 1
        else:
            score += 1
            ace_count -= 1
    return score


def one_round():
    suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
    values = ['A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck = []
    for s in suits:
        for v in values:
            c = Cards(s, v)
            deck.append(Cards.face(c))

    Dealer = []
    Hand = []

    new_card(Dealer, deck)
    print("Dealer's hand: ", Dealer)
    new_card(Dealer, deck)
    new_card(Hand, deck)
    new_card(Hand, deck)

    print("Your hand:", Hand)
    print("score:", score_calc(Hand))

    while score_calc(Hand) < 21:
        i = input("Hit or stand? ")
        if i.upper() == 'HIT':
            new_card(Hand, deck)
            print(Hand)
            print(score_calc(Hand))
        elif i.upper() == 'STAND':
            break
    if score_calc(Hand) > 21:
        print("BUST!")
        return 'loss'
    else:
        player_score = score_calc(Hand)
        dealer_score = score_calc(Dealer)
        print("Your hand is", Hand, "with a value of", player_score)
        print("The Dealer's hand is", Dealer, "with a value of", dealer_score)
        while dealer_score < 17:
            new_card(Dealer, deck)
            dealer_score = score_calc(Dealer)
            print("The Dealer's hand is", Dealer, "with a value of", dealer_score)
        if dealer_score > 21 or player_score > dealer_score:
            print("Congratulations! You win!")
            return 'win'
        elif player_score < dealer_score:
            print("Bad luck! :(")
            return 'loss'
        elif player_score == dealer_score:
            print('Push')
            return 'tie'


def game():
    balance = int(input("How much money would you like to play with? "))
    while balance > 0:
        print("Balance:", balance)
        bet = int(input("bet? "))
        rnd = one_round()
        if rnd == 'win':
            balance += int(bet)
        elif rnd == 'loss':
            balance -= int(bet)

game()