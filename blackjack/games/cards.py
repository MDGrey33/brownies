from random import shuffle

suites = ('of Clubs', 'of Hearts', 'of Spades', 'of Diamonds')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# Face Down card is a card of value zero used to replace a face down card in calculations
rank_to_value = {'Two': 2, 'Three': 3, 'Four': 4,
                 'Five': 5, 'Six': 6, 'Seven': 7,
                 'Eight': 8, 'Nine': 9, 'Ten': 10,
                 'Jack': 10, 'Queen': 10, 'King': 10,
                 'Ace': 11, 'Face Down': 0}


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank
        self.value = rank_to_value[self.rank]
        self.face_up = True

    def set_face_up(self, value=True):
        self.face_up = value

    def __str__(self):
        return f'{self.rank} {self.suite}'


class Deck:

    def __init__(self):
        self.cards = [Card(suite, rank) for suite in suites for rank in ranks]

    def shuffle(self):
        shuffle(self.cards)

    def deal_cards(self):
        return self.cards.pop()


class Shoe:
    def __init__(self, deck_count):
        self.cards = []
        for x in range(deck_count):
            self.cards.extend(Deck().cards)

    def shuffle(self, shuffle_times):
        for x in range(shuffle_times):
            shuffle(self.cards)

    def deal_card(self, face_up=True):
        if not face_up:
            self.cards[0].set_face_up(False)
        return self.cards.pop(0)

    def __str__(self):
        return f'Shoe has {len(self.cards)} cards!'


class Hand:
    def __init__(self):
        self.cards = []
        self.bet = 0
        self.bust = False
        self.face_down_card = Card('Card', 'Face Down')
        self.face_down_card.set_face_up(False)

    @property
    def cards_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            if card.rank == 'Ace':
                ace_count += 1
            value += card.value
            if not card.face_up:
                value -= card.value
            while value > 21 and ace_count > 0:
                ace_count -= 1
                value -= 10

        return value

    def add_card(self, one_card):
        self.cards.append(one_card)

    def return_card_index(self, card_rank, card_suite):
        i = 0
        for card in self.cards:
            if card.rank == card_rank and card_suite == card_suite:
                return i
            i += 1

    def remove_card(self, card_index):
        self.cards.pop(card_index)

    def show_card(self, index):
        return self.cards[index]

    def show_cards(self):
        card_list = []
        for card in self.cards:
            if not card.face_up:
                card_list.append(self.face_down_card)
            else:
                card_list.append(card)
        return card_list

    def add_bet(self, amount):
        self.bet += amount

    def reset_bet(self):
        self.bet = 0

    def set_bust(self, bool_value):
        self.bust = bool_value
        return self.bust

    def __str__(self):
        return f'His hand has {len(self.cards)} cards with {self.bet}$ bet on it\nHand Value: {self.cards_value}'


class Player:
    def __init__(self, name, money_amount=1000):
        self.name = name
        self.hand = Hand()
        self.bankroll = money_amount

    def bet_on_hand(self, bet_amount):
        self.bankroll -= bet_amount
        self.hand.add_bet(bet_amount)

    def give_money(self, amount):
        self.bankroll -= amount
        return amount

    def add_money(self, amount):
        self.bankroll += amount

    def wins_double(self, bet_amount):
        self.bankroll += (2 * bet_amount)

    def wins(self, bet_amount):
        self.bankroll += bet_amount

    def looses_double(self, bet_amount):
        self.bankroll -= (2 * bet_amount)

    def looses(self, bet_amount):
        self.bankroll -= bet_amount

    def push(self, bet_amount):
        self.bankroll += bet_amount

    def reset_for_new_round(self):
        self.hand = Hand()

    def __str__(self):
        return f'{self.name} has {self.bankroll} $ in his bankroll'
