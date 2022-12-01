from random import shuffle


suites = ('Clubs', 'Hearts', 'Spades', 'Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
rank_to_value = {'Two': 2, 'Three': 3, 'Four': 4,
                 'Five': 5, 'Six': 6, 'Seven': 7,
                 'Eight': 8, 'Nine': 9, 'Ten': 10,
                 'Jack': 11, 'Queen': 12,
                 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = rank_to_value[self.rank]

    def __str__(self):
        return f'{self.rank} of {self.suite}'


def deal_cards(card_deck):
    shuffle(card_deck)
    split = len(card_deck) // 2
    first_hand_cards = card_deck[:split]
    second_hand_cards = card_deck[split:]
    return first_hand_cards, second_hand_cards


def print_cards(cards):
    i = 0
    for card in cards:
        i += 1
        print(card, i)