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


class Deck:

    def __init__(self):
        self.cards = [Card(suite, rank) for suite in suites for rank in ranks]

    def shuffle(self):
        shuffle(self.cards)

    def deal_cards(self, amount):
        card_list =[]
        while not amount == 0:
            card_list.append(self.cards.pop())
            amount -= 1
        return card_list


def print_cards(cards):
    i = 0
    for card in cards:
        i += 1
        print(card, i)
