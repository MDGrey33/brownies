from games.view import *


my_player = Player('John', 1001)
my_table = Table(my_player)
my_table.show_information('Bet')
my_table.show_actions('Bet')
my_player.hand.add_card(my_table.shoe.deal_card())
my_player.hand.add_card(my_table.shoe.deal_card())
my_table.dealer.hand.add_card(my_table.shoe.deal_card(False))
my_table.dealer.hand.add_card(my_table.shoe.deal_card())
my_table.show_information('Game')
my_table.show_actions("Game")