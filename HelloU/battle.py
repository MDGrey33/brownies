from games.cards import Deck


def attack():
    print(first_hand_cards[0], ' Vs', second_hand_cards[0], 'Attack')
    if first_hand_cards[0].value > second_hand_cards[0].value:
        first_hand_cards.append(second_hand_cards.pop(0))
        print(f'second hand lost 1 card')
    else:
        second_hand_cards.append(first_hand_cards.pop(0))
        print(f'first hand lost 1 card')


def battle():
    print(first_hand_cards[1], ' Vs', second_hand_cards[1], 'Battle')
    """
        Check if both hands have enough cards for war otherwise redirect to attack 
    """
    if len(first_hand_cards) <= 1 or len(second_hand_cards) <= 1:
        print('Not enough cards for a battle, this will be an attack instead')
        attack()
    elif first_hand_cards[1].value > second_hand_cards[1].value:
        first_hand_cards.append(second_hand_cards.pop(0))
        first_hand_cards.append(second_hand_cards.pop(0))
        print(f'second hand lost 2 cards')
    else:
        second_hand_cards.append(first_hand_cards.pop(0))
        second_hand_cards.append(first_hand_cards.pop(0))
        print(f'first hand lost 2 cards ')


def announce_winner():
    if len(first_hand_cards) > len(second_hand_cards):
        print(f'\nFirst hand won\nFirst hand: {len(first_hand_cards)} Vs Second hand: {len(second_hand_cards)}')
    else:
        print(f'\nSecond hand won\nSecond hand: {len(second_hand_cards)} Vs First hand: {len(first_hand_cards)}')


card_deck = Deck()
card_deck.shuffle()
first_hand_cards = card_deck.deal_cards(26)
second_hand_cards = card_deck.deal_cards(26)

while len(first_hand_cards) > 0 and len(second_hand_cards) > 0:
    print(f'\nFirst hand: {len(first_hand_cards)} \nSecond hand: {len(second_hand_cards)}')
    if first_hand_cards[0].value == second_hand_cards[0].value:
        battle()
    else:
        attack()

announce_winner()
