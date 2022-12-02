from games.cards import Deck, Player


def attack():
    print(player_one.cards[0], ' Vs', player_two.cards[0], 'Attack')
    if player_one.cards[0].value > player_two.cards[0].value:
        player_one.add_cards(player_two.remove_one())
        print(f'{player_two.name} lost 1 card')
    else:
        player_two.add_cards(player_one.remove_one())
        print(f'{player_one.name} lost 1 card')


def battle():
    print(player_one.cards[0], ' Vs', player_two.cards[0], 'Battle')
    """
        Check if both hands have enough cards for war otherwise redirect to attack 
    """
    if len(player_one.cards) <= 1 or len(player_one.cards) <= 1:
        print('Not enough cards for a battle, this will be an attack instead')
        attack()
    elif player_one.cards[1].value > player_one.cards[1].value:
        player_one.add_cards(player_two.remove_one())
        player_one.add_cards(player_two.remove_one())
        print(f'{player_two.name} lost 2 cards')
    else:
        player_two.add_cards(player_one.remove_one())
        player_two.add_cards(player_one.remove_one())
        print(f'{player_one.name} lost 2 cards ')


def announce_winner():
    if len(player_one.cards) > len(player_two.cards):
        print(f'\nWinner {player_one} Vs Loser {player_two}')
    else:
        print(f'\nWinner {player_two} Vs Loser {player_one}')


# Initiate the players
player_one = Player('John')
player_two = Player('Mary')

# Initiate the deck and shuffle
card_deck = Deck()
card_deck.shuffle()

# Distribute the cards
player_one.add_cards(card_deck.deal_cards(26))
player_two.add_cards(card_deck.deal_cards(26))

# Run the game till one of the players runs out of cards
while len(player_one.cards) > 0 and len(player_two.cards) > 0:
    print(player_one, '\n', player_two)
    # If both players cards are equal initiate a battle otherwise initiate an attack
    if player_one.cards[0] == player_two.cards[0]:
        battle()
    else:
        attack()

# Announce the winner
announce_winner()
