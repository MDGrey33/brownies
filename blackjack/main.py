from games.view import *


my_player = Player('John', 1001)
"""dealer = Player('Dealer', 1000000)
player.bet_on_hand(1000)
dealer.add_money(player.hand.bet)
player.hand.reset_bet()
print(dealer.bankroll)
print(player.hand.bet)
print(player.bankroll)"""


my_table = Table(my_player)
game_on = True
while game_on:
    answer = (input('Are you ready to play(Y/N)')).capitalize()
    if answer == 'N':
        break
    elif answer == 'Y':
        my_player.reset_for_new_round()
        my_table.dealer.reset_for_new_round()
    my_table.show_information('Bet')
    my_table.show_actions('Bet')
    my_player.hand.add_card(my_table.shoe.deal_card())
    my_player.hand.add_card(my_table.shoe.deal_card())
    my_table.dealer.hand.add_card(my_table.shoe.deal_card(False))
    my_table.dealer.hand.add_card(my_table.shoe.deal_card())
    my_table.show_information('Game')
    my_table.show_actions('Game')
    # Accounting
    my_table.show_information('Account')
    my_table.show_actions('Account')
