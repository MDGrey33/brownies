# Refactor to make sure a played card goes back to the bottom

from games.cards import Deck, Player


def attack():
    print(f'\n{player_one.name} drew the {player_one.cards[0]} while '
          f'{player_two.name} drew the {player_two.cards[0]} in an attack')
    if player_one.cards[0].value > player_two.cards[0].value:
        player_one.add_cards(player_two.remove_one())
        print(f'{player_two.name} lost 1 card')
    else:
        player_two.add_cards(player_one.remove_one())
        print(f'{player_one.name} lost 1 card')


def battle():
    battle_flag = True
    while battle_flag:
        print(f'\n{player_one.name} drew the {player_one.cards[0]} while '
              f'{player_two.name} drew the {player_two.cards[0]} in a battle')
        """
            Check if both hands have enough cards for war otherwise redirect to attack 
        """
        if len(player_one.cards) <= 1 or len(player_two.cards) <= 1:
            print('Not enough cards for a battle, this will be an attack instead')
            attack()
            battle_flag = False
        elif player_one.cards[1].value > player_two.cards[1].value:
            print(f'then {player_one.name} drew the {player_one.cards[1]} while '
                  f'{player_two.name} drew the {player_two.cards[1]} in a battles second move')
            player_one.add_cards(player_two.remove_one())
            player_one.add_cards(player_two.remove_one())
            print(f'{player_two.name} lost 2 cards')
            battle_flag = False
        elif player_two.cards[1].value > player_one.cards[1].value:
            print(f'then {player_one.name} drew the {player_one.cards[1]} while '
                  f'{player_two.name} drew the {player_two.cards[1]} in a battles second move')
            player_two.add_cards(player_one.remove_one())
            player_two.add_cards(player_one.remove_one())
            print(f'{player_one.name} lost 2 cards ')
            battle_flag = False


def announce_winner():
    if len(player_one.cards) > len(player_two.cards):
        print(f'\n{player_one.name} won!')
    else:
        print(f'\n{player_two.name} won!')


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
    print(f'{player_one} \n{player_two}')
    # If both players cards are equal initiate a battle otherwise initiate an attack
    if player_one.cards[0].value == player_two.cards[0].value:
        battle()
    else:
        attack()

# Announce the winner
announce_winner()
