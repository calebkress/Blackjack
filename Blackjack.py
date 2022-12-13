import random

suits = ('Hearts', 'Spades', 'Diamonds', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = { 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

isGameActive = True

# define Card class
class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self): 
        return self.rank + ' of ' + self.suit

# define Deck class
class Deck:
    def __init__(self): 
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has: ' + deck_comp
    def shuffle(self): 
        random.shuffle(self.deck)
    def deal(self): 
        dealt_card = self.deck.pop()
        return dealt_card

# define Hand class
class Hand: 
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card): 
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# define Chips class
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
    
# function to take player's bet
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError: 
            print('Sorry, a bet must be an integer value.')
        else:
            if chips.bet > chips.total:
                print('Sorry, your bet can\'t exceed ', chips.total)
            else:
                break

# function to handle player hit
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# function to ask player to hit or stand
def hit_or_stand(deck, hand):
    global isGameActive
    while True: 
        x = input('Would you like to hit or stand? Enter \'h\' or \'s\': ')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer is playing.')
        else: 
            print('Sorry, please try again.')
            continue
        break


