from blackjack.games.cards import *


black_jack_views = {'Bet': 'Place your bets',
                    'Game': 'Bet until all hands are satisfied',
                    'Account': 'Account for hand results'}
betting_chips = {'1000': 1000, '500': 500, '100': 100,
                 '50': 50, '25': 25, '5': 5, '1': 1}


class Table:
    def __init__(self, player):
        self.shoe = Shoe(6)
        self.dealer = Player('Dealer', 1000000)
        self.views = [black_jack_views.keys()]
        self.player = player

    def show_information(self, view):
        if view == 'Bet':
            print(self.shoe)
            print(self.player)

        elif view == 'Game':
            print(self.shoe)
            print('\n')
            print(self.dealer.name)
            print(f'His hand has {len(self.dealer.hand.cards)} cards')
            for card in self.dealer.hand.show_cards():
                if not card.face_up:
                    print('Face Down Card')
                else:
                    print(card)
            print('\n')
            print(self.player)
            print(self.player.hand)
            for card in self.player.hand.show_cards():
                if not card.face_up:
                    print('Face Down Card')
                else:
                    print(card)
            print('\n')

        elif view == 'Account':
            print(self.shoe)
            print(self.dealer)
            print(self.dealer.hand)
            print(self.player)
            print(self.player.hand)

    def show_actions(self, view):
        if view == 'Bet':
            self.player.bet_on_hand(int(input('How much do you want to start your bet with?')))
        if view == 'Game':
            pass
            # is it a blackjack? --> accounting
            # Show Hit, Stand, Double