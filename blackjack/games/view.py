from blackjack.games.cards import *
import time


class Table:
    def __init__(self, player):
        self.shoe = Shoe(6)
        self.shoe.shuffle(6)
        self.dealer = Player('Dealer', 1000000)
        self.player = player
        self.blackjack = False
        self.players = [self.dealer, self.player]

    # Accounting Actions
    def player_wins(self, bet_amount):
        self.player.wins(bet_amount)
        self.dealer.looses(bet_amount)
        self.player.push(bet_amount)

    def player_wins_double(self, bet_amount):
        self.player.wins_double(bet_amount)
        self.dealer.looses_double(bet_amount)
        self.player.push(bet_amount)

    def dealer_wins(self, bet_amount):
        self.dealer.wins(bet_amount)

    def push(self, bet_amount):
        self.player.push(bet_amount)

    # Show views
    def show_information(self, view):
        if view == 'Bet':
            print(self.shoe)
            print(f'You have {self.player.bankroll}$ in your bankroll')
        elif view == 'Game':

            print(self.shoe)
            print('\n')
            for player in self.players:
                print(player.name)
                print(player.hand)
                for card in player.hand.show_cards():
                    print(card)
                print('\n')
            time.sleep(1)
        elif view == 'Account':
            for player in self.players:
                print(player, player.hand)
        else:
            print('The page you requested is not found')

    # Action views
    def show_actions(self, view):

        if view == 'Bet':
            valid_input = False
            while not valid_input:
                bet = input('How much do you want to start your bet with?')
                if bet.isdigit() and 0 < int(bet) <= self.player.bankroll:
                    bet = int(bet)
                    valid_input = True
            self.player.bet_on_hand(bet)
        elif view == 'Game':
            game_on = True
            self.player.hand.set_bust(False)
            while game_on and not self.player.hand.bust and not self.blackjack:
                if self.player.hand.cards_value == 21:
                    self.blackjack = True
                    break
                else:
                    while self.player.hand.cards_value < 21 and game_on:
                        action = input(
                            f'your hand Value is: {self.player.hand.cards_value}\nchose(1 or 2):\n1.X Stand\n2.+ Hit\n')
                        if action == '1':
                            game_on = False
                            break
                        elif action == '2':
                            self.player.hand.add_card(self.shoe.deal_card())
                            self.show_information('Game')
                        else:
                            print('Please try again.')
                    game_on = False
                    time.sleep(3)
            # Dealers game
            self.dealer.hand.cards[0].set_face_up(True)
            if self.player.hand.cards_value > 21:
                self.player.hand.set_bust(True)
            if not self.player.hand.bust and not self.blackjack:
                game_on = True

            while game_on:
                if self.dealer.hand.cards_value == 21:
                    break
                else:
                    while self.dealer.hand.cards_value < 17 and game_on:
                        self.dealer.hand.add_card(self.shoe.deal_card())
                        self.show_information('Game')
                        time.sleep(1)
                    game_on = False
                    time.sleep(2)
        elif view == 'Account':
            bet_amount = self.player.hand.bet
            if self.player.hand.cards_value == 21:
                self.player_wins_double(bet_amount)

            elif self.player.hand.cards_value > 21:
                self.dealer_wins(bet_amount)

            elif self.dealer.hand.cards_value > 21:
                self.player_wins(bet_amount)

            elif self.player.hand.cards_value > self.dealer.hand.cards_value:
                self.player_wins(bet_amount)

            elif self.player.hand.cards_value < self.dealer.hand.cards_value:
                self.dealer_wins(bet_amount)

            elif self.player.hand.cards_value == self.dealer.hand.cards_value:
                self.push(bet_amount)

            else:
                print('We have a problem in accounting.')
            self.player.hand.reset_bet()
            print('Accounting completed')
            self.show_information('Account')
