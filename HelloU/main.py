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


def deal_cards():
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


def attack():
    print(first_hand_cards[0], ' Vs', second_hand_cards[0], 'Attack')
    if first_hand_cards[0].value > second_hand_cards[0].value:
        second_hand_cards.pop(0)
        print(f'attack concluded second hand lost {len(second_hand_cards)}')
    else:
        first_hand_cards.pop(0)
        print(f'attack concluded first hand lost {len(first_hand_cards)}')


def battle():
    print(first_hand_cards[1], ' Vs', second_hand_cards[1], 'Battle')
    if first_hand_cards[1].value > second_hand_cards[1].value:
        second_hand_cards.pop(0)
        second_hand_cards.pop(0)
        print(f'battle concluded second hand lost 2 cards {len(second_hand_cards)}')
    else:
        first_hand_cards.pop(0)
        first_hand_cards.pop(0)
        print(f'attack concluded first hand lost 2 cards {len(first_hand_cards)}')


def announce_winner():
    if len(first_hand_cards) > len(second_hand_cards):
        print(f'First hand won\n First hand: {len(first_hand_cards)} Vs Second hand: {len(second_hand_cards)}')
    else:
        print(f'Second hand won\nSecond hand: {len(second_hand_cards)} Vs First hand: {len(first_hand_cards)}')


card_deck = [Card(suite, rank) for suite in suites for rank in ranks]
first_hand_cards, second_hand_cards = deal_cards()
while len(first_hand_cards) > 0 and len(second_hand_cards) > 0:
    print(f'\nFirst hand: {len(first_hand_cards)} Vs Second hand: {len(second_hand_cards)}')
    if first_hand_cards[0].value == second_hand_cards[0].value:
        battle()
    else:
        attack()


announce_winner()
