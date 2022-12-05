from blackjack.games.cards import *
import time


black_jack_views = {'Bet': 'Place your bets',
                    'Game': 'Bet until all hands are satisfied',
                    'Account': 'Account for hand results'}
betting_chips = {'1000': 1000, '500': 500, '100': 100,
                 '50': 50, '25': 25, '5': 5, '1': 1}


class Table:
    def __init__(self, player):
        self.shoe = Shoe(6)
        self.shoe.shuffle(6)
        self.dealer = Player('Dealer', 1000000)
        self.views = [black_jack_views.keys()]
        self.player = player
        self.blackjack = False
        self.bust = False

    def show_information(self, view):
        if view == 'Bet':
            print(self.shoe)
            print(self.player)

        elif view == 'Game':
            print(self.shoe)
            print('\n')
            time.sleep(1)
            print(self.dealer.name)
            print(f'His hand has {len(self.dealer.hand.cards)} cards')
            for card in self.dealer.hand.show_cards():
                if not card.face_up:
                    print('Face Down Card')
                else:
                    print(card)
            print('\n')
            time.sleep(1)
            print(self.player)
            print(self.player.hand)
            for card in self.player.hand.show_cards():
                if not card.face_up:
                    print('Face Down Card')
                else:
                    print(card)
            print('\n')
            time.sleep(3)

        elif view == 'Account':
            # print(self.shoe)
            print(f'{self.dealer} {self.dealer.hand}\nHand value: {self.dealer.hand.cards_value}')
            print(f'{self.player} {self.player.hand}\nHand value: {self.player.hand.cards_value}')

        else:
            print('The page you requested is not found')

    def show_actions(self, view):
        if view == 'Bet':
            self.player.bet_on_hand(int(input('How much do you want to start your bet with?')))
        elif view == 'Game':
            game_on = True
            bust = False
            while game_on and not bust and not self.blackjack:
                if self.player.hand.cards_value == 21:
                    self.blackjack = True
                    break
                else:
                    while self.player.hand.cards_value < 21 and game_on:
                        action = input(f'your hand Value is: {self.player.hand.cards_value}\nchose(1 or 2):\n1.X Stand\n2. + Hit ')
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
                self.bust = True
            if not self.bust and not self.blackjack:
                game_on = True

            while game_on:
                if self.dealer.hand.cards_value == 21:
                    break
                else:
                    while self.dealer.hand.cards_value < 17 and game_on:
                        self.dealer.hand.add_card(self.shoe.deal_card())
                        self.show_information('Game')
                        time.sleep(3)
                    game_on = False
                    time.sleep(3)
        elif view == 'Account':
            if self.player.hand.cards_value == 21:
                self.player.add_money(self.player.hand.bet)
                self.player.add_money(self.dealer.give_money(self.player.hand.bet*2))
                self.player.hand.reset_bet()
            elif self.player.hand.cards_value > 21:
                self.dealer.add_money(self.player.hand.bet)
                self.player.hand.reset_bet()
            elif self.dealer.hand.cards_value > 21:
                self.player.add_money(self.dealer.give_money(self.player.hand.bet))
                self.player.hand.reset_bet()
            elif self.player.hand.cards_value > self.dealer.hand.cards_value:
                self.player.add_money(self.dealer.give_money(self.player.hand.bet))
                self.player.hand.reset_bet()
            elif self.player.hand.cards_value < self.dealer.hand.cards_value:
                self.dealer.add_money(self.player.hand.bet)
                self.player.hand.reset_bet()
            else:
                print('We have a problem in accounting.')
            self.show_information('Account')
            print('accounting successful')
